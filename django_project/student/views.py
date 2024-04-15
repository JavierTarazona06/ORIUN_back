from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentApplicationSerializer


class ApplicationDataView(APIView):
    """
    API endpoint that allows to get and put data related to the contact info and medical information
    of the student
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if not hasattr(request.user, 'student'):
            return Response('Current user is not a student', status=status.HTTP_404_NOT_FOUND)

        student = request.user.student
        serializer = StudentApplicationSerializer(student)
        return Response(serializer.data)

    def put(self, request):
        if not hasattr(request.user, 'student'):
            return Response('Current user is not a student', status=status.HTTP_404_NOT_FOUND)

        student = request.user.student
        serializer = StudentApplicationSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
