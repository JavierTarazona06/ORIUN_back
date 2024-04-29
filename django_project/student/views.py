import json

from call.models import Call
from rest_framework import status

from .models import Student
from .permissions import IsStudent
from django.http import JsonResponse
from rest_framework import permissions
from datetime import datetime, timezone
from rest_framework.views import APIView
from application.models import Application
from rest_framework.response import Response
from .serializers import StudentApplicationSerializer, StudentSerializer, StudentSerializerGeneral
from django.contrib.auth.models import User


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
            return JsonResponse({'eligibility': False, 'message': 'Usted pertenece al nivel de estudios necesario'})

        if call.university.get_region_display() == 'Uniandes':
            if student.num_semesters < 2:
                return JsonResponse(
                    {'eligibility': False, 'message': 'Para esta convocatoria necesita minimo 2 semestres cursados'}
                )
        else:
            if student.advance < call.min_advance:
                return JsonResponse({'eligibility': False, 'message': 'PAPA insuficiente'})

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


class post_user_student(APIView):
    permission_classes = []
    serializer = StudentSerializer()

    def post(self, request):
        input_params = json.loads(request.body)
        input_params['username'] = input_params["email"]

        user = User.objects.create_user(
            username=input_params['username'],
            email=input_params['email'],
            password=input_params['password'],
            first_name=input_params['first_name'],
            last_name=input_params['last_name'],
        )
        input_params["user"] = user
        del input_params["username"]
        del input_params["email"]
        del input_params["password"]
        del input_params["first_name"]
        del input_params["last_name"]

        certificates = [input_params["certificate_grades"], input_params["certificate_student"],
                        input_params["payment_receipt"]]
        del input_params["certificate_grades"]
        del input_params["certificate_student"]
        del input_params["payment_receipt"]

        verif_code = input_params["verif_code"]
        del input_params["verif_code"]

        input_params['birth_date'] = datetime.strptime(input_params['birth_date'], '%Y-%m-%d').date()

        serializer = StudentSerializer(data=input_params)

        print(input_params)
        print(certificates)


        Student.objects.create(**input_params)

        qset = Student.objects.filter(id=1041578941)
        qset = StudentSerializerGeneral(qset, many=True).data
        print(qset)


        return JsonResponse({'mensaje', 'Estudiante creado exitosamente'}, status=200, safe=False)
