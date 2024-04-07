from rest_framework import permissions
from signin.serializers import MyTokenObtainPairSerializer

class IsEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.employee:
            return request.method