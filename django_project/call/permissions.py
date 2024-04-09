from rest_framework import permissions
from signin.serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from employee.models import Employee

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, User):
            return Employee.objects.filter(user=user).exists()
        return False