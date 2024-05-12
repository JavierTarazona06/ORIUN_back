import os

from call.models import Call
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .models import Student
from .permissions import IsStudent
from django.http import JsonResponse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import permissions
from datetime import datetime, timezone
from rest_framework.views import APIView
from application.models import Application
from rest_framework.response import Response
from .serializers import StudentApplicationSerializer, StudentSerializer, StudentGetSerializer
from django.contrib.auth.models import User
from application.helpers import upload_object, get_link_file
from data import helpers
from data.constants import Constants
from person.serializers import UserSerializerShort
from traceability.models import Traceability
from traceability.serializers import TraceabilitySerializer


class EligibilityView(APIView):
    """
    API endpoint that allows to get and put data related to the contact info and medical information
    of the student
    """
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request):
        student = request.user.student

        # Being matriculated or en 'reserva de cupo'
        if not student.is_enrolled:
            return JsonResponse({'eligibility': False, 'message': 'Necesita estar matriculado o en reserva de cupo'})

        # Max applications in a semester
        year, month = datetime.now(timezone.utc).strftime('%Y %m').split(" ")
        semester = '1' if int(month) <= 6 else '2'
        if len(Application.objects.filter(student_id=student, year=int(year), semester=semester)) == 2:
            return JsonResponse({'eligibility': False, 'message': 'Ya tiene el máximo de postulaciones en 1 semestre'})

        # Banned by UN or ORI
        if datetime.utcnow().date() <= student.date_banned_mobility:
            return JsonResponse({'eligibility': False, 'message': 'No puede participar debido a la sanción que posee'})

        # Initial requirements: min PAPA, study level, advance, etc
        call = Call.objects.get(pk=request.GET.get('call'))
        if student.PAPA < call.min_papa:
            return JsonResponse({'eligibility': False, 'message': 'PAPA insuficiente'})
        if student.study_level != call.study_level:
            return JsonResponse({'eligibility': False, 'message': 'Usted no pertenece al nivel de estudios necesario'})

        if call.university.get_region_display() == 'Uniandes':
            if student.num_semesters < 2:
                return JsonResponse(
                    {'eligibility': False, 'message': 'Para esta convocatoria necesita minimo 2 semestres cursados'}
                )
        else:
            if student.advance < call.min_advance:
                return JsonResponse({'eligibility': False, 'message': 'Avance insuficiente'})

        return JsonResponse({'eligibility': True, 'message': ''})


class ApplicationDataView(APIView):
    """
    API endpoint that allows to get and put data related to the contact info and medical information
    of the student
    """
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request):
        student = request.user.student
        serializer = StudentApplicationSerializer(student)
        return Response(serializer.data)

    def put(self, request):
        student = request.user.student
        serializer = StudentApplicationSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data has been updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadUserStudent(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request, pk):
        try:
            my_student = Student.objects.get(pk=pk)
            if not (request.user.email == my_student.user.email):
                raise ValidationError("El usuario {} no tiene permiso para ver la información del usuario solicitado".format(request.user))
            my_student_qset = Student.objects.filter(pk=pk)
            my_student_sr = StudentGetSerializer(my_student_qset, many=True).data[0]

            applications_qset = Application.objects.filter(student__id=my_student.id)
            calls_list = applications_qset.values('call__id', 'call__university__name', 'call__study_level',
                                                  'call__year', 'call__semester', 'call__description')
            calls_done = list(calls_list)
            my_student_sr['calls_done'] = calls_done

            certificates = Student.certificates
            certificates_names = [
                str(my_student.id) + '_' + str(certificates[0]),
                str(my_student.id) + '_' + str(certificates[1]),
                str(my_student.id) + '_' + str(certificates[2])
            ]

            bucket = 'student_certificates'
            certificates_links = [
                get_link_file(bucket, certificates_names[0]),
                get_link_file(bucket, certificates_names[1]),
                get_link_file(bucket, certificates_names[2])
            ]

            my_student_sr[certificates[0][:-4]] = certificates_links[0]
            my_student_sr[certificates[1][:-4]] = certificates_links[1]
            my_student_sr[certificates[2][:-4]] = certificates_links[2]

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": datetime.now(),
                "method": request.method,
                "view": "ReadUserStudent",
                "given_data": f"El usuario solicito la información del estudiante con id {my_student.id}."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(my_student_sr, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class post_user_student(APIView):
    permission_classes = []
    serializer = StudentSerializer()

    def post(self, request):
        input_params = request.data
        input_params = dict(input_params)

        for key, value in input_params.items():
            if str(type(value)) == "<class 'list'>":
                input_params[key] = value[0]

        username = input_params["email"]
        try:
            if not "@unal.edu.co" in input_params["email"]:
                raise ValueError("El correo no es dominio @unal.edu.co")

            # Verification Code -----
            if "verif_code" not in input_params:
                raise ValueError("No se envío el código de verificación enviado al correo")
            else:
                verif_code_sent = input_params["verif_code"]
                del input_params["verif_code"]
                code_file_name = r"data/{}_verif_code.txt".format(input_params["id"])
                with open(code_file_name, "r") as file:
                    code_stored = file.read()
                if not (code_stored==verif_code_sent):
                    raise ValidationError("El código de verificación de acceso enviado al correo no concuerda con el ingresado")

            # Creating User -----
            input_params['username'] = input_params["email"]
            user = User.objects.create_user(
                username=input_params['username'],
                email=input_params['email'],
                password=input_params['password'],
                first_name=input_params['first_name'],
                last_name=input_params['last_name'],
            )
            input_params["user"] = user.id
            del input_params["username"]
            del input_params["email"]
            del input_params["password"]
            del input_params["first_name"]
            del input_params["last_name"]

            # Dividing certificates -----
            # if input_params["certificate_grades"].size > 3_000_000:
            #     raise ValidationError("File grades is too big. It must be smaller than 3 MB")
            # if input_params["certificate_student"].size > 3_000_000:
            #     raise ValidationError("File student is too big. It must be smaller than 3 MB")
            # if input_params["payment_receipt"].size > 3_000_000:
            #     raise ValidationError("File payment is too big. It must be smaller than 3 MB")
            # certificates = {
            #     "grades": input_params["certificate_grades"].file,
            #     "student": input_params["certificate_student"].file,
            #     "payment": input_params["payment_receipt"].file
            # }


            # Divide and Upload Certificates
            grades_file_name = str(input_params["id"]) + '_' + str(Student.certificates[0])
            helpers.base_64_to_pdf(input_params["certificate_grades"], grades_file_name)
            with open(grades_file_name, 'rb') as grades_file:
                grades_data = grades_file.read()
                grades_obj = SimpleUploadedFile("Certificado_Notas.pdf", grades_data)

            student_file_name = str(input_params["id"]) + '_' + str(Student.certificates[1])
            helpers.base_64_to_pdf(input_params["certificate_student"], student_file_name)
            with open(student_file_name, 'rb') as student_file:
                student_data = student_file.read()
                student_obj = SimpleUploadedFile("Certificado_Matricula_Estudiante.pdf", student_data)

            payment_file_name = str(input_params["id"]) + '_' + str(Student.certificates[2])
            helpers.base_64_to_pdf(input_params["payment_receipt"], payment_file_name)
            with open(payment_file_name, 'rb') as payment_file:
                payment_data = payment_file.read()
                payment_obj = SimpleUploadedFile("Recibo_Pago.pdf", payment_data)

            del input_params["certificate_grades"]
            del input_params["certificate_student"]
            del input_params["payment_receipt"]

            certificates = {
                "grades": grades_obj.file,
                "student": student_obj.file,
                "payment": payment_obj.file
            }

            upload_object('student_certificates', certificates["grades"], grades_file_name)
            upload_object('student_certificates', certificates["student"], student_file_name)
            upload_object('student_certificates', certificates["payment"], payment_file_name)

            # Certificates Validation
            # with open(grades_file_name, "wb") as pdf_file:
            #     pdf_file.write(certificates["grades"].getvalue())
            # with open(student_file_name, "wb") as pdf_file:
            #     pdf_file.write(certificates["student"].getvalue())
            # with open(payment_file_name, "wb") as pdf_file:
            #     pdf_file.write(certificates["payment"].getvalue())

            data_from_grades = helpers.get_data_grades_certificate(grades_file_name)
            data_from_student = helpers.get_data_student_certificate(student_file_name)
            data_from_payment = helpers.get_data_student_payment(payment_file_name)
            os.remove(grades_file_name)
            os.remove(student_file_name)
            os.remove(payment_file_name)


            # Data Validation -----
            # input_params['birth_date'] = datetime.strptime(input_params['birth_date'], '%Y-%m-%d').date()
            # input_params = dict(input_params)
            # for key, value in input_params.items():
            #     if str(type(value)) == "<class 'datetime.date'>":
            #         input_params[key] = value.strftime("%Y-%m-%d")
            #     if str(type(value)) == "<class 'int'>":
            #         input_params[key] = str(value)
            #     else:
            #         input_params[key] = value[0]

            # Validation Serializer -----
            serializer = StudentSerializer(data=input_params)
            if not serializer.is_valid():
                errors = serializer.errors
                raise ValueError(str(errors))
            input_params["user"] = user

            # Validate PDFs
            valid_id = ((str(data_from_grades['id']) == str(input_params['id'])) and (
                        data_from_student['id'] == str(input_params['id']))
                        and (data_from_payment['id'] == str(input_params['id'])))
            if not valid_id:
                raise ValueError("El ID no concuerda con el certificado.")

            valid_average = (data_from_grades['average'] == str(input_params['PAPA']))
            if not valid_average:
                raise ValueError("El promedio no concuerda con el certificado.")

            std_program = ''
            for opt in Constants.MAJOR_CHOICES:
                if opt["value"] == input_params['major']:
                    std_program = opt["display"]
                    break
            valid_program = (data_from_grades['program'].upper() == std_program.upper())
            if not valid_program:
                raise ValueError(
                    "El programa no concuerda con el certificado o hay problema con la lista almacenada de programas.")

            valid_faculty = (data_from_grades['faculty'].upper() == input_params['faculty'].upper())
            if not valid_faculty:
                raise ValueError(
                    "La facultad no concuerda con el certificado o hay problema con la lista almacenada de facultades.")

            valid_advance = (data_from_student['advance'] == str(input_params['advance']))
            if not valid_advance:
                raise ValueError("El avance no concuerda con el certificado.")

            valid_pbm = (data_from_payment['pbm'] == str(input_params['PBM']))
            if not valid_pbm:
                raise ValueError("El valor de PBM no concuerda con el certificado.")

            val_admi = ''
            data_from_payment['admission'] = data_from_payment['admission'].upper()
            if "PAES" in data_from_payment['admission']:
                val_admi = "PAES"
            elif "PEAMA" in data_from_payment['admission']:
                val_admi = "PEAMA"
            elif "REGUL" in data_from_payment['admission']:
                val_admi = "REGUL"
            else:
                raise ValueError("El string de admisión no se reconoció como PAES/PEAMA/REGUL.")
            valid_admission = (val_admi == input_params['admission'])
            if not valid_admission:
                raise ValueError("El string de admisión no concuerda con el certificado.")

            # Create Student -----
            Student.objects.create(**input_params)

            this_student = Student.objects.get(id=input_params['id'])
            this_user = this_student.user
            data_trace = {
                "user": this_user,
                "time": datetime.now(),
                "method": request.method,
                "view": "PostUserEmployee",
                "given_data": f"Se creó al usuario estudiante con id {this_student.id} con correo {this_student.user.email} e id usuario {this_student.user.id}."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse({'mensaje': 'Estudiante creado exitosamente'}, status=status.HTTP_200_OK)
        except Exception as e:
            try:
                user_inst = User.objects.get(username=username)
            except User.DoesNotExist:
                pass
            else:
                user_inst.delete()
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
