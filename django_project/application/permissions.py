from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    message = 'Current user is not a student'

    def has_permission(self, request, view):
        return hasattr(request.user, 'student')


class IsEmployee(permissions.BasePermission):
    message = 'Current user is not a employee'

    def has_permission(self, request, view):
        return hasattr(request.user, 'employee')