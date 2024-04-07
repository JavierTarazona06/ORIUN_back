#from rest_framework import viewsets
import json

from rest_framework import generics, permissions
from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .permissions import IsEmployee


from .models import Call, University
from .serializer import CallSerializer, UniversitySerializer


class CallView(generics.ListCreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

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
            queryset = queryset.filter(university_id__language=language)
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