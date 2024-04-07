#from rest_framework import viewsets
from rest_framework import generics
from .models import Call, University
from .serializer import CallSerializer, UniversitySerializer


class CallView(generics.ListCreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class CallDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class UniversityView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer