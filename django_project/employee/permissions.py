from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    message = 'Current user is not an Employee'

    def has_permission(self, request, view):
        return hasattr(request.user, 'employee')