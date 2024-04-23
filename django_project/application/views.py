from .helpers import *
from rest_framework import status
from .permissions import IsStudent
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from student.views import ApplicationDataView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes, parser_classes


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
def get_region_call(request: Request):
    """
    Endpoint used to get the region (Uniandes, Nacional, Internacional) given a call. Lets the
    front know which documents should be asked to the user.
    """
    call_id = request.query_params['call']
    call = Call.objects.get(id=call_id)
    region = call.university_id.get_region_display()
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

    # Check student has a contact_id
    student = request.user.student
    contact_person = student.contact_id
    if contact_person is None:
        return JsonResponse({'error': 'La persona de contacto no ha sido definida'}, status=status.HTTP_400_BAD_REQUEST)

    # Set up the attributes (from student model and the ones that came in the request)
    attributes = set_variables(request, student)

    # Create folder for saving the files (only for the initial creation)
    call = Call.objects.get(id=request.data['call'])
    path_original_forms = os.path.join('forms', 'original_forms')
    path_save_forms = os.path.join('forms', f'{student.id}_{call.id}')

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

    short_name = Constants.NAME_FORMS[name_file]
    name_object = f'{short_name}_{student.id}_{call.id}.docx'

    try:
        link_form = get_link_file(type_file, name_object)
        return JsonResponse({'link': link_form}, status=status.HTTP_200_OK)
    except FileNotFoundError:
        return JsonResponse({'message': 'form not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsStudent])
@parser_classes([MultiPartParser, FormParser])
def upload_file(request: Request):
    """
    Endpoint used to upload a file to GCP. The new name is composed of the name parameter (in query),
    the id of the student, the id of the call and the original extension of the file.
    """
    student = request.user.student
    call = Call.objects.get(id=request.data['call'])
    source_file = request.data['file'].file
    source_extension = request.data['file'].name.split('.')[-1]
    name_file = request.data['name']

    new_name = f'{name_file}_{student.id}_{call.id}.{source_extension}'

    upload_object('complete_documents', source_file, new_name)
    return Response({'message': 'File uploaded successfully!'}, status=status.HTTP_200_OK)
