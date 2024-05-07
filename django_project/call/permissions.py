from rest_framework import permissions
from django.contrib.auth.models import User
from employee.models import Employee

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, User):
            return Employee.objects.filter(user=user).exists()
        return False

class IsStudent(permissions.BasePermission):
    message = 'Current user is not a student'

    def has_permission(self, request, view):
        return hasattr(request.user, 'student')