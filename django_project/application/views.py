import io
import base64

from datetime import datetime, timezone
from urllib.request import Request
from django.http import QueryDict

from google.cloud import exceptions as gcloud_exceptions

from datetime import timezone, timedelta
import pytz
from django.db.models import Q

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from google.cloud import exceptions as gcloud_exceptions
from rest_framework import permissions, generics, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes


from student.views import ApplicationDataView
from .permissions import IsStudent, IsEmployee
from .serializers import ApplicationSerializer, ApplicationModifySerializer, StateSerializer, \
    ApplicationDetailSerializer, ApplicationOrdersSerializer, ApplicationResults


from .helpers import *
from . import serializers
from call.models import Call
from .models import Application
from student.models import Student
from traceability.models import Traceability
from student.views import ApplicationDataView
from .permissions import IsStudent, IsEmployee
from data.helpers import send_email_winner, send_email_not_winner, get_col_time
from .serializers import (
    ApplicationModifySerializer, StateSerializer, ApplicationOrdersSerializer, Applicants
)

HOUR_COL = get_col_time()

def save_traceability(request: Request, name_view: str, description: str) -> None:
    data_trace = {
        "user": request.user,
        "time": HOUR_COL,
        "method": request.method,
        "view": name_view,
        "given_data": description
    }
    Traceability.objects.create(**data_trace)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_region_call(request: Request):
    """
    Endpoint used to get the region (Uniandes, Nacional, Internacional) given a call. Lets the
    front know which documents should be asked to the user.
    """
    call_id = request.query_params['call']
    call = Call.objects.get(id=call_id)
    region = call.university.get_region_display()

    save_traceability(
        request, 'get_region_call', f'El usuario solicito ver los documentos de la convocatoria {call_id}'
    )

    if region == 'Uniandes':
        return JsonResponse({'region': 'Uniandes'}, status=status.HTTP_200_OK)
    elif region == 'Convenio Sigueme/Nacional':
        return JsonResponse({'region': 'Nacional'}, status=status.HTTP_200_OK)
    return JsonResponse({'region': 'Internacional'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
def create_forms(request: Request):
    """
    Endpoint used to save the student data such as contact person and health information,
    fill out the forms accordingly to the body given in the request and save them in the cloud.
    """
    # Set the contact person and health information of the student
    response = ApplicationDataView().put(request)
    if response.status_code != status.HTTP_200_OK:
        return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

    # Check student has a contact_person
    student = request.user.student
    contact_person = student.contact_person
    if contact_person is None:
        return JsonResponse({'error': 'La persona de contacto no ha sido definida'}, status=status.HTTP_400_BAD_REQUEST)

    save_traceability(
        request, 'create_forms', f"El usuario actualizó sus datos personales y de contacto, y solicitó"
                                 f"crear los formularios de la convocatoria {request.data['call']}"
    )

    # Set up the attributes (from student model and the ones that came in the request)
    attributes = set_variables(request, student)

    # Create folder for saving the files (only for the initial creation)
    call = Call.objects.get(id=request.data['call'])
    path_original_forms = os.path.join('data', 'forms', 'templates')
    path_save_forms = os.path.join('data', 'forms', f'{student.id}_{call.id}')

    # Fill up forms, upload them to the cloud and remove them from system
    fill_forms(attributes, path_original_forms, path_save_forms)
    upload_forms(path_save_forms)

    return Response({'message': 'Forms filled successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
def download_file(request: Request):
    """
    Endpoint used to get a link to a form given a call, student and type of form (if it is a filled
    one or the original).
    """
    student = request.user.student
    call_id = request.query_params['call']
    call = Call.objects.get(id=call_id)
    name_file = request.query_params['name_file']
    type_file = request.query_params['type_file']

    if type_file == 'original_doc':
        name_object = f'{name_file}'
    else:
        name_object = f'{name_file}_{student.id}_{call.id}'

    save_traceability(
        request, 'download_file', f'El usuario solicito el archivo {name_object}'
    )

    try:
        link_form = get_link_file(type_file, name_object)
        return JsonResponse({'link': link_form}, status=status.HTTP_200_OK)
    except FileNotFoundError:
        return JsonResponse({'message': 'form not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def upload_file(request: Request):
    """
    Endpoint used to upload a file to GCP. The new name is composed of the name parameter (in query),
    the id of the student, the id of the call and the original extension of the file.
    """
    # Check size of document
    '''if request.data['document'].size > 9_000_000:
        return Response(
            {'error': 'File is too big. It must be smaller than 9 MB'}, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
        )
    '''
    student = request.user.student
    call = Call.objects.get(id=request.data['call'])

    try:
        _, data = request.data['document'].split(',')
    except ValueError:
        data = request.data['document']
    source_file = io.BytesIO(base64.b64decode(data))
    name_file = request.data['name_file']
    new_name = f'{name_file}_{student.id}_{call.id}.pdf'

    save_traceability(
        request, 'upload_file', f'El usuario subio el archivo {new_name}'
    )

    upload_object('complete_doc', source_file, new_name)
    return Response({'message': 'File uploaded successfully!'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
def submit_application(request: Request):
    """
    Endpoint used to make sure that all the documents have been submitted correctly, and for
    creating the application for the student.
    """
    # TODO: add case when the deadline is over and the application can not be created
    student = request.user.student
    call = Call.objects.get(id=request.data['call'])

    is_complete, missing_docs = check_docs(student, call)
    if not is_complete:
        name_missing_docs = ' '.join(str(i) for i in missing_docs)
        return Response({'message': f'Missing uploading {name_missing_docs}'}, status=status.HTTP_404_NOT_FOUND)

    # Add missing data for serializer
    data = request.data.copy()
    data['student'] = student.id
    data['year'], month = datetime.now(timezone.utc).strftime('%Y %m').split(" ")
    data['semester'] = '1' if int(month) <= 6 else '2'

    # Create application
    serializer = serializers.ApplicationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    save_traceability(
        request, 'submit_application', f'El usuario creo una aplicacion para la convocatoria {call.id}'
    )

    return Response({'message': 'Application created'}, status=status.HTTP_200_OK)


class ApplicationComments(generics.ListAPIView):
    """
    Endpoint used to return the comments made from an employee for a specific application.
    """
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request, *args, **kwargs):
        student = self.request.user.student
        call = self.request.query_params['call']
        application = Application.objects.get(student=student, call=call)
        serializer = serializers.ApplicationComments(application)

        save_traceability(
            request, 'ApplicationComments', f'El usuario solicito los comentarios de la aplicacion {application.id}'
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
def edit_application(request: Request):
    """
    Endpoint used to replace a document on GCP with the given document.
    """
    # Check size of document
    student = request.user.student
    call = Call.objects.get(id=request.data['call'])
    application = Application.objects.filter(student=student, call=call).update(modified=True)

    # Delete previous document
    try:
        _, data = request.data['document'].split(',')
    except ValueError:
        data = request.data['document']
    source_file = io.BytesIO(base64.b64decode(data))
    name_file = request.data['name_file']
    name = f'{name_file}_{student.id}_{call.id}'
    delete_object('complete_doc', name)

    # Upload new document
    new_name = f'{name_file}_{student.id}_{call.id}.pdf'
    upload_object('complete_doc', source_file, new_name)

    save_traceability(
        request, 'edit_application', f'El usuario edito el documento {name_file} de la aplicación {application.id}'
    )

    return Response({'message': 'Document updated'}, status=status.HTTP_200_OK)


# ------------------------------------------------ case10 --------------------------------------------

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def applicants(request, call_id):
    """
    Endpoint used to retrieve applicants for a specific call based on provided filters.
    Filters can be applied to narrow down the search criteria.
    """
    serializer = Applicants(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    try:
        applications = Application.objects.filter(call_id=call_id).order_by('state_documents')
        if not applications.exists():
            return Response({"error": "No applications found for the provided call ID"},
                            status=status.HTTP_404_NOT_FOUND)

        # Apply filters from query parameters:)
        filters = request.query_params.dict()

        applications = applications.filter(**filters)

        save_traceability(
            request, 'applicants', f'El funcionario solicito las aplicaciones de la convocatoria {call_id}'
                                   f'con los filtros {filters}'
        )

        serializer = Applicants(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def documents(request, call_id, student_id):
    """
    Endpoint used to retrieves documents associated with a student's
    application for a specific call.
    """
    try:
        application = Application.objects.get(call_id=call_id, student_id=student_id)
    except Application.DoesNotExist:
        return JsonResponse({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)

    call = Call.objects.get(id=call_id)
    region = call.university.get_region_display()

    documents = {}
    if region == 'Uniandes':
        doc_names = Application.name_docs
    elif region == 'Convenio Sigueme/Nacional':
        doc_names = Application.national_name_docs + Application.name_docs
    else:
        doc_names = Application.international_name_docs + Application.name_docs

    for doc_name in doc_names:
        try:
            link = get_link_file('complete_doc', f"{doc_name}")
            documents[doc_name] = link

        except gcloud_exceptions.Forbidden:
            return JsonResponse({'error': f'URL expiration time has passed for file "{doc_name}"'},
                                status=status.HTTP_400_BAD_REQUEST)
        except FileNotFoundError:
            return JsonResponse({'error': f'File "{doc_name}" not found'}, status=status.HTTP_404_NOT_FOUND)

    response_data = {
        'call_id': call_id,
        'student_id': student_id,
        'documents': documents
    }

    save_traceability(
        request, 'documents', f'El funcionario solicito todos los documentos de la convocatoria {call_id}'
                              f'del estudiante {student_id}'
    )

    return JsonResponse(response_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def modify(request, call_id, student_id):
    """
    Endpoint used to request modifications to an existing student application
    """
    try:
        application = Application.objects.get(call_id=call_id, student_id=student_id)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {'state_documents': '1', 'modified': False}
    serializer = ApplicationModifySerializer(application, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        save_traceability(
            request, 'modify', f'El funcionario solicito modificar los documentos de la aplicacion {application.id}'
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def accept_documents(request, call_id, student_id):
    """
    Endpoint to accept documents for a specific student's application
    """
    try:
        application = Application.objects.get(call_id=call_id, student_id=student_id)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Set the value of state_documents to 2 for accepting documents
    data = {'state_documents': 2, 'modified': False}
    serializer = ApplicationModifySerializer(application, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        save_traceability(
            request, 'accept_documents', f'El funcionario acepto los documentos de la aplicacion {application.id}'
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def get_student_info(request, student_id, call_id):
    """
    Endpoint to retrieve student information related to an application
    """
    try:
        student = Application.objects.get(call_id=call_id, student_id=student_id)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Applicants(student)
    save_traceability(
        request, 'get_student_info', f'El funcionario solicito la informacion del estudiante de la '
                                     f'aplicacion {student.id}'
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def get_state(request, call_id, student_id):
    """
    Endpint to  retrieve the state of a student application based on the provided call_id and student_id.

    State Values:
    - 0: Application not yet reviewed.
    - 1: Modification requested by the student.
    - 2: Application accepted.
    - 3: Modifications made by the student.
       """
    try:
        application = Application.objects.get(call_id=call_id, student_id=student_id)
        # Check modified and determine state (Not reviewed: 0, Modify: 1, Accepted:2)
        if application.modified:
            state = 3
        elif application.state_documents == 0:
            state = 0
        elif application.state_documents == 1:
            state = 1
        elif application.state_documents == 2:
            state = 2
        else:
            state = None

        serializer = StateSerializer(
            data={'call': application.call_id, 'student_id': application.student_id, 'state': state})
        serializer.is_valid()

        save_traceability(
            request, 'get_state', f'El funcionario solicito el estado de la aplicacion {application.id}'
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def add_comment(request, call_id, student_id):
    """
    Endpoint to add a comment to a student's application for a specific call.
    """
    try:
        application = Application.objects.get(call_id=call_id, student_id=student_id)
    except Application.DoesNotExist:
        return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

    comment = request.data.get('comment')
    application.comment = comment
    application.save()

    save_traceability(
        request, 'add_comment', f'El funcionario coloco el comentario {comment} en la aplicacion {application.id}'
    )
    return Response({"message": "Comment added successfully."}, status=status.HTTP_201_CREATED)


class OrderDocs(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk).order_by('-state_documents')
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por estado de documentación de los estudiantes."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderPAPA(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk).order_by('-student__PAPA')
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por PAPA descendente de los estudiantes."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderAdvance(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk).order_by('-student__advance')
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por porcentaje de avance de carrera de los estudiantes."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderLanguage(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk).order_by('-state_documents')
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por cumplimiento del requisito de idioma de los estudiantes."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderPBM(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk).order_by('student__PBM')
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por PBM ascendente de los estudiantes."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderGeneral(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk).order_by('-state_documents', '-student__PAPA',
                                                                        '-student__advance', 'student__PBM')
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por estado de la documentación, PAPA, Avance, Idioma y PBM de los estudiantes (Orden General)."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetAllApplications(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            applications = Application.objects.filter(call=pk)
            applications = ApplicationOrdersSerializer(applications, many=True).data

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó las aplicaciones a la convocatoria {pk} ordenadas por estado de la documentación, PAPA, Avance, Idioma y PBM de los estudiantes (Orden General)."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(applications, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SetWinner(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def post(self, request):
        try:
            input_params = request.data
            this_application = Application.objects.get(call_id=input_params['call_id'],
                                                       student_id=input_params['student_id'])

            # Verificar que los estudiantes ya fueron revisados
            se_puede_asignar_ganador(input_params['call_id'])

            # Check Available Slots
            call_applications = Application.objects.filter(call=this_application.call_id)
            quant_stud_approved = 0
            for i in range(len(call_applications)):
                if (call_applications[i].approved):
                    quant_stud_approved += 1
            if this_application.call.available_slots < (quant_stud_approved + 1):
                raise AttributeError(
                    f"No se pueden aceptar mas estudiantes. Estudiantes ya Aceptados: {quant_stud_approved}. Cupos: {this_application.call.available_slots}")

            # Set Winner
            this_application.approved = True
            this_application.save()

            # Close the call
            this_call = Call.objects.get(id=this_application.call_id)
            this_call.active = False
            this_call.save()

            # Send email
            student_winner = Student.objects.get(id=this_application.student.id)
            send_email_winner(student_winner.user.email,
                              str(student_winner.user.first_name) + ' ' + str(student_winner.user.last_name),
                              this_call.id, this_call.university.name, this_call.year, this_call.semester)

            # Modify Highest and minimum PAPA winner in Call
            this_call = Call.objects.get(id=this_application.call_id)
            if this_call.highest_papa_winner < student_winner.PAPA:
                this_call.highest_papa_winner = student_winner.PAPA
            if this_call.minimum_papa_winner > student_winner.PAPA:
                this_call.minimum_papa_winner = student_winner.PAPA
            this_call.save()

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario seleccionó al estudiante con id {student_winner.id} como ganador de la convocatoria {this_call.id}."
            }
            Traceability.objects.create(**data_trace)
            return JsonResponse({
                "message": f"El estudiante con ID {input_params['student_id']} fue seleccionado para la convocatoria {this_application.call_id}"},
                status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RemoveWinner(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def post(self, request):
        try:
            input_params = request.data

            # Remove as winner
            this_application = Application.objects.get(call__id=input_params['call_id'],
                                                       student_id=input_params['student_id'])
            this_application.approved = False
            this_application.save()

            # Send email
            student_not_winner = Student.objects.get(id=this_application.student.id)
            this_call = Call.objects.get(id=this_application.call_id)
            send_email_not_winner(student_not_winner.user.email, str(student_not_winner.user.first_name) + ' ' + str(
                student_not_winner.user.last_name), this_call.id, this_call.university.name, this_call.year,
                                  this_call.semester)

            # Modify Highest and minimum PAPA winner in Call
            all_applications_this_call = Application.objects.filter(call__id=input_params['call_id'], approved=True)

            if this_call.highest_papa_winner == student_not_winner.PAPA:
                max_papa = 0
                for application in all_applications_this_call:
                    if application.student.PAPA > max_papa:
                        max_papa = application.student.PAPA
                this_call.highest_papa_winner = max_papa

            if this_call.minimum_papa_winner == student_not_winner.PAPA:
                min_papa = 5
                for application in all_applications_this_call:
                    if application.student.PAPA < min_papa:
                        min_papa = application.student.PAPA
                this_call.minimum_papa_winner = min_papa

            this_call.save()

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario des-seleccionó al estudiante con id {student_not_winner.id} como ganador de la convocatoria {this_call.id}."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse({
                "message": f"El estudiante con ID {input_params['student_id']} fue des-seleccionado para la convocatoria {this_application.call_id}"},
                status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OriunError(Exception):
    def __init__(self, message="Hay un error en las Aplicaciones de ORIUN"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'OriunError: {self.message}'


def se_puede_asignar_ganador(call_id) -> bool:
    pending_applications = Application.objects.filter(
        Q(call__id=call_id, state_documents=0) |
        Q(call__id=call_id, state_documents=1, modified=True)
    )
    pending_applications = ApplicationOrdersSerializer(pending_applications, many=True).data

    if len(pending_applications) > 0:
        raise OriunError(
            "Hay estudiantes que tienen aplicaciones pendientes por revisar. Aún no se puede asignar ganador. Estudiantes: " + str(
                pending_applications))

    return True

class PreAssignWinners(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            se_puede_asignar_ganador(pk)

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": self.__class__.__name__,
                "given_data": f"El usuario solicitó confirmación para asignar ganadores de una convocatoria."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse({"message": "Ya se revisaron todas las aplicaciones, se pueden asignar los ganadores"},
                                status=status.HTTP_200_OK, safe=True)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



#CASE 8 ---------------------------------------------
class ApplicationsStudent(generics.GenericAPIView):
    """
    Endpoint used to return the student's applications in reverse chronological order and with general
    information about the application.
    """
    permission_classes = [permissions.IsAuthenticated, IsStudent]
    serializer_class = serializers.StudentCalls

    def get(self, request, *args, **kwargs):
        try:
            student = self.request.user.student

            application = Application.objects.filter(student=student).order_by('-year', '-semester').first()

            if not application:
                return Response({"error": "No applications found for this student."}, status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
def results(request: Request, call_id):
    """
            Endpoint to retrieve results if the student is accepted, not accepted or pending application verification
    """
    serializer = Applicants(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    try:
        student = request.user.student
        application = Application.objects.get(student=student, call=call_id)
    except Application.DoesNotExist:
        return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)


    if application.approved is True:
        message = f"Felicitaciones, usted ha sido seleccionad@ a la convocatoria {call_id}."
    elif application.approved is False:
        message = f"Lo sentimos, usted no ha sido seleccionad@ a la convocatoria {call_id}."
    else:
        message = f"Su aplicación está pendiente de revisión para la convocatoria {call_id}."

    serializer = ApplicationDetailSerializer(application)

    save_traceability(
        request, 'results', f'El estudiante con id:{student},  solicito los resultados para la convocatoria: {call_id} .'
    )
    return Response({"message": message, "application": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def results_employee(request: Request, call_id):
    """
    Endpoint to retrieve all applications with corresponding result, in case it has been accepted or not
    """
    try:
        # TODO: add case when the application is closed

        serializer = Applicants(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        approved = request.GET.get('approved')

        applications = Application.objects.filter(call_id=call_id)

        if approved is not None:
            applications = applications.filter(approved=approved).order_by('approved')

        #applications = applications.order_by('approved')

        if not applications.exists():
            return Response({"error": "No results found for the provided call ID"},
                            status=status.HTTP_404_NOT_FOUND)

        filters = request.query_params.dict()
        applications = applications.filter(**filters)

        serializer = ApplicationResults(applications, many=True)

        save_traceability(
            request, 'results_employee', f'El funcionario solicito los resultados de la convocatoria {call_id}'
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

