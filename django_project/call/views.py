
#from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Call, University
from .serializers import CallSerializerOpen, CallSerializerClosed, CallDetailsSerializerOpenStudent, CallDetailsSerializerClosedStudent, CallSerializer, UniversitySerializer
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
import json
from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsEmployee


class OpenCallsStudent(APIView):
    def get(self, request):

        try:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthenticated user'}, status=status.HTTP_401_UNAUTHORIZED)
            student = request.user.student

            if student.is_banned_behave_un:
                return JsonResponse({'error': 'You are banned from accessing open calls.'},
                                    status=status.HTTP_403_FORBIDDEN)

            student_papa = request.user.student.PAPA
            student_study_level = request.user.student.study_level
            student_advance = request.user.student.advance

            call_id = request.GET.get('id')
            country = request.GET.get('country')
            language = request.GET.get('language')
            university_name = request.GET.get('name_university')

            if university_name:
                university_name = university_name.lower()

            # Filter open calls based on provided criteria (OPEN CALLS)
            open_calls = Call.objects.filter(active=True)

            if call_id:
                open_calls = open_calls.filter(id=call_id)
            if country:
                open_calls = open_calls.filter(university_id__country=country)
            if language:
                open_calls = open_calls.filter(language=language)
            if university_name:
                open_calls = open_calls.filter(university_id__name__icontains=university_name)

            open_calls = open_calls.filter(min_papa__lte=student_papa)
            open_calls = open_calls.filter(study_level=student_study_level)
            open_calls = open_calls.filter(min_advance__lte=student_advance)

            # Serialize the filtered calls using the serializer
            serializer = CallSerializerOpen(open_calls, many=True)
            # Check if there are no calls that match the criteria
            if not open_calls.exists():
                return JsonResponse({'message': 'No calls match the provided criteria'},
                                    status=status.HTTP_404_NOT_FOUND)
            # Return JSON response
            return JsonResponse(serializer.data, safe=False)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



class ClosedCallsStudent(APIView):
    def get(self,request):
        try:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthenticated user'}, status=status.HTTP_401_UNAUTHORIZED)
            student = request.user.student

            country = request.GET.get('country')
            language = request.GET.getlist('language')
            name_university = request.GET.get('name_university')
            min_papa_winner = request.GET.get('minimum_papa_winner')

            # Filter calls based on provided criteria (CLOSED CALLS)
            closed_calls = Call.objects.filter(active=False)

            if country:
                closed_calls = closed_calls.filter(university_id__country=country)

            if language:
                closed_calls = closed_calls.filter(language=language)

            if name_university:
                closed_calls = closed_calls.filter(university_id__name__icontains=name_university)

            if min_papa_winner:
                closed_calls = closed_calls.filter(minimum_papa_winner__gte=float(min_papa_winner))

            # Serialize the data
            serializer_closed = CallSerializerClosed(closed_calls, many=True)
            # Check if there are no calls that match the criteria
            if not closed_calls.exists():
                return JsonResponse({'message': 'No calls match the provided criteria'},
                                    status=status.HTTP_404_NOT_FOUND)

            # Return JSON response
            return JsonResponse(serializer_closed.data, safe=False)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class OpenCallDetailStudent(APIView):
    def get(self, request, id):
        try:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthenticated user'}, status=status.HTTP_401_UNAUTHORIZED)
            student = request.user.student

            # obtain the specific open call by its ID
            open_call = Call.objects.filter(id=id, active=True).first()
            serializer = CallDetailsSerializerOpenStudent(open_call)

            if open_call is None:
                return JsonResponse({'message': 'No calls match the provided criteria'},
                                    status=status.HTTP_404_NOT_FOUND)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class ClosedCallDetailStudent(APIView):
    def get(self, request, id):
        try:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthenticated user'}, status=status.HTTP_401_UNAUTHORIZED)
            student = request.user.student

            # obtain the specific open call by its ID
            close_call = Call.objects.filter(id=id, active=False).first()
            serializer = CallDetailsSerializerClosedStudent(close_call)

            if close_call is None:
                return JsonResponse({'message': 'No calls match the provided criteria'},
                                    status=status.HTTP_404_NOT_FOUND)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Javi

class CallView(generics.ListCreateAPIView):
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get_queryset(self):
        queryset = Call.objects.all()
        if self.request.method == 'POST':
            university_id = self.request.data.get('university_id', None)
            if university_id is not None:
                queryset = queryset.filter(university_id=university_id)
        return queryset


class CallDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

class OpenCalls(generics.ListCreateAPIView):
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]
    def get_queryset(self):
        current_date = timezone.now().date()
        return Call.objects.filter(deadline__gte=current_date, active=True)

class ClosedCalls(generics.ListCreateAPIView):
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]
    def get_queryset(self):
        current_date = timezone.now().date()
        return Call.objects.filter(Q(deadline__lt=current_date) | Q(active=False))
    

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsEmployee])
def CallsFilterSearch(request):
    try:
        active = request.data.get('active')
        university_id = request.data.get('university_id')
        university_name = request.data.get('university_name')
        deadline = request.data.get('deadline')
        format = request.data.get('format')
        study_level = request.data.get('study_level')
        year = request.data.get('year')
        semester = request.data.get('semester')
        region = request.data.get('region')
        country = request.data.get('country')
        language = request.data.get('language')
        
        if university_name:
            university_name = university_name.lower()

        # Construct queryset based on parameters
        queryset = Call.objects.all()

        if active:
            queryset = queryset.filter(active=active)        
        if university_id:
            queryset = queryset.filter(university_id__id=university_id)
        if deadline:
            queryset = queryset.filter(deadline__lte=deadline)
        if format:
            queryset = queryset.filter(format=format)
        if study_level:
            queryset = queryset.filter(study_level=study_level)
        if year:
            queryset = queryset.filter(year=year)
        if semester:
            queryset = queryset.filter(semester=semester)
        if region:
            queryset = queryset.filter(university_id__region=region)
        if country:
            queryset = queryset.filter(university_id__country=country)
        if language:
            queryset = queryset.filter(language=language)
        if university_name:
            queryset = queryset.filter(university_id__name__icontains=university_name)
    
        serializer = CallSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    except Exception as e:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    
class UniversityView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

