#from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Call, University
from .serializers import CallSerializerOpen, CallSerializerClosed, CallDetailsSerializerOpenStudent, \
    CallDetailsSerializerClosedStudent, CallSerializer, UniversitySerializer
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
import json
from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsEmployee
from employee.models import Employee
from django.contrib.auth.models import User
from data.constants_dict_front import constants_dict_front
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime



class OpenCallsStudent(APIView):
    def get(self, request):

        try:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthenticated user'}, status=status.HTTP_401_UNAUTHORIZED)
            student = request.user.student

            student_papa = request.user.student.PAPA
            student_study_level = request.user.student.study_level
            student_advance = request.user.student.advance

            countries = request.GET.get('countries')
            languages = request.GET.get('languages')
            university_name = request.GET.get('name_university')

            if university_name:
                university_name = university_name.lower()

            # Filter open calls based on provided criteria (OPEN CALLS)
            open_calls = Call.objects.filter(active=True)

            if countries:
                open_calls = open_calls.filter(university__country__in=countries.split(','))
            if languages:
                open_calls = open_calls.filter(language__in=languages.split(','))
            if university_name:
                open_calls = open_calls.filter(university__name__icontains=university_name)

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
    def get(self, request):
        try:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthenticated user'}, status=status.HTTP_401_UNAUTHORIZED)
            student = request.user.student

            country = request.GET.get('country')
            language = request.GET.get('language')
            name_university = request.GET.get('name_university')
            min_papa_winner = request.GET.get('minimum_papa_winner')

            # Filter calls based on provided criteria (CLOSED CALLS)
            closed_calls = Call.objects.filter(active=False)

            if country:
                closed_calls = closed_calls.filter(university__country=country)

            if language:
                closed_calls = closed_calls.filter(language=language)

            if name_university:
                closed_calls = closed_calls.filter(university__name__icontains=name_university)

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

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)

    def get_queryset(self):
        return Call.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        for call in queryset:
            call.format = constants_dict_front["format"][str(call.format)]
            call.study_level = constants_dict_front["study_level"][str(call.study_level)]
            call.language = constants_dict_front["language"][str(call.language)]

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class CallDetails(generics.RetrieveUpdateDestroyAPIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.queryset = Call.objects.all()
            self.serializer_class = CallSerializer
            self.permission_classes = [permissions.IsAuthenticated, IsEmployee]
        except Exception as e:
            self.handle_exception(e)

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.format = constants_dict_front["format"][str(instance.format)]
        instance.study_level = constants_dict_front["study_level"][str(instance.study_level)]
        instance.language = constants_dict_front["language"][str(instance.language)]

        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        try:
            call = Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CallSerializer(instance=call, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCallsView(View):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            return None

    def put(self, request, pk):
        call = self.get_object(pk)
        if not call:
            return JsonResponse({'error': 'La convocatoria especificada no existe'}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))

            if 'university_id' in data:
                university_id = int(data['university_id'])
                try:
                    university_instance = University.objects.get(pk=university_id)
                except University.DoesNotExist:
                    return JsonResponse({'error': 'La universidad especificada no existe'}, status=400)
                call.university = university_instance
            if 'active' in data:
                call.active = data['active']
            if 'begin_date' in data:
                call.begin_date = data['begin_date']
            if 'deadline' in data:
                call.deadline = data['deadline']
            if 'min_advance' in data:
                call.min_advance = data['min_advance']
            if 'min_papa' in data:
                call.min_papa = data['min_papa']
            if 'format' in data:
                call.format = data['format']
            if 'study_level' in data:
                call.study_level= data['study_level']
            if 'year' in data:
                call.year = data['year']
            if 'semester' in data:
                call.semester = data['semester']
            if 'language' in data:
                call.language = data['language']
            if 'description' in data:
                call.description = data['description']
            if 'available_slots' in data:
                call.available_slots = data['available_slots']
            if 'note' in data:
                call.note = data['note']
            if 'highest_papa_winner' in data:
                call.highest_papa_winner = data['highest_papa_winner']
            if 'minimum_papa_winner' in data:
                call.minimum_papa_winner = data['minimum_papa_winner']
            if 'selected' in data:
                call.selected = data['selected']

            call.save()
            return JsonResponse({'mensaje': 'Convocatoria actualizada exitosamente'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)


class OpenCalls(generics.ListCreateAPIView):
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get_queryset(self):
        current_date = timezone.now().date()
        return Call.objects.filter(deadline__gte=current_date, active=True)

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        for call in queryset:
            call.format = constants_dict_front["format"][str(call.format)]
            call.study_level = constants_dict_front["study_level"][str(call.study_level)]
            call.language = constants_dict_front["language"][str(call.language)]

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class ClosedCalls(generics.ListCreateAPIView):
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get_queryset(self):
        current_date = timezone.now().date()
        return Call.objects.filter(Q(deadline__lt=current_date) | Q(active=False))

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        for call in queryset:
            call.format = constants_dict_front["format"][str(call.format)]
            call.study_level = constants_dict_front["study_level"][str(call.study_level)]
            call.language = constants_dict_front["language"][str(call.language)]

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class CallsFilterSearch(APIView):
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request):
        try:
            active = request.GET.get('active')
            university_id = request.GET.get('university_id')
            university_name = request.GET.get('university_name')
            deadline = request.GET.get('deadline')
            format = request.GET.get('formato')
            study_level = request.GET.get('study_level')
            year = request.GET.get('year')
            semester = request.GET.get('semester')
            region = request.GET.get('region')
            country = request.GET.get('country')
            language = request.GET.get('language')

            if university_name:
                university_name = university_name.lower()

            # Construct queryset based on parameters
            queryset = Call.objects.all()

            if active:
                if (active == "true"):
                    active = "T" + active[1:]
                if (active == "false"):
                    active = "F" + active[1:]
                queryset = queryset.filter(active=active)
            if university_id:
                queryset = queryset.filter(university__id=university_id)
            if deadline:
                queryset = queryset.filter(deadline__lte=deadline)
            if format:
                if format == "P":
                    queryset = queryset.filter(format='P')
                elif format == "V":
                    queryset = queryset.filter(format='V')
                elif format == "M":
                    queryset = queryset.filter(format='M')
                #queryset = queryset.filter(format=format)
            if study_level:
                queryset = queryset.filter(study_level=study_level)
            if year:
                queryset = queryset.filter(year=year)
            if semester:
                queryset = queryset.filter(semester=semester)
            if region:
                queryset = queryset.filter(university__region=region)
            if country:
                queryset = queryset.filter(university__country__icontains=country)
            if language:
                queryset = queryset.filter(language=language)
            if university_name:
                queryset = queryset.filter(university__name__icontains=university_name)

            if not queryset.exists():
                return JsonResponse({'message': 'No calls match the provided criteria'},
                                    status=status.HTTP_404_NOT_FOUND)

            for call in queryset:
                call.format = constants_dict_front["format"][str(call.format)]
                call.study_level = constants_dict_front["study_level"][str(call.study_level)]
                call.language = constants_dict_front["language"][str(call.language)]

            serializer = CallSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class UniversityView(generics.ListCreateAPIView):
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)

    def get_queryset(self):
        return University.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        for university in queryset:
            university.region = constants_dict_front["region"][str(university.region)]

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class UniversityDetails(generics.RetrieveUpdateDestroyAPIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.queryset = University.objects.all()
            self.serializer_class = UniversitySerializer
            self.permission_classes = [permissions.IsAuthenticated, IsEmployee]
        except Exception as e:
            self.handle_exception(e)

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)

    def put(self, request, pk):
        try:
            university = University.objects.get(pk=pk)
        except University.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UniversitySerializer(instance=university, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.region = constants_dict_front["region"][str(instance.region)]

        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)


class UpdateUniversityView(View):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return University.objects.get(pk=pk)
        except University.DoesNotExist:
            return None

    def put(self, request, pk):
        university = self.get_object(pk)
        if not university:
            return JsonResponse({'error': 'La universidad especificada no existe'}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))

            if 'name' in data:
                university.name = data['name']
            if 'webpage' in data:
                university.webpage = data['webpage']
            if 'region' in data:
                university.region = data['region']
            if 'country' in data:
                university.country = data['country']
            if 'city' in data:
                university.city = data['city']
            if 'academic_offer' in data:
                university.academic_offer = data['academic_offer']
            if 'exchange_info' in data:
                university.exchange_info = data['exchange_info']

            university.save()
            return JsonResponse({'mensaje': 'Universidad actualizada exitosamente'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Solicitud JSON no válida'}, status=400)
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, exc):
        return JsonResponse({'error': str(exc)}, status=500)