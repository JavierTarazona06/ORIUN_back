from call.models import Call
from rest_framework import status
from .permissions import IsStudent
from django.http import JsonResponse
from rest_framework import permissions
from datetime import datetime, timezone
from rest_framework.views import APIView
from application.models import Application
from rest_framework.response import Response
from .serializers import StudentApplicationSerializer


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
        semester = '1' if int(month) <= 6 else '1'
        if len(Application.objects.filter(student_id=student, year=int(year), semester=semester)) == 2:
            return JsonResponse({'eligibility': False, 'message': 'Ya tiene el máximo de postulaciones en 1 semestre'})

        # Banned by UN or ORI
        if student.is_banned_behave_un or datetime.utcnow().date() <= student.date_banned_mobility:
            return JsonResponse({'eligibility': False, 'message': 'No puede participar debido a la sanción que posee'})

        # Initial requirements: min PAPA, study level, advance, etc
        call = Call.objects.get(pk=request.GET.get('call'))
        if student.PAPA < call.min_papa:
            return JsonResponse({'eligibility': False, 'message': 'PAPA insuficiente'})
        if student.study_level != call.study_level:
            return JsonResponse({'eligibility': False, 'message': 'Usted pertenece al nivel de estudios necesario'})

        if call.university_id.get_region_display() == 'Uniandes':
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
