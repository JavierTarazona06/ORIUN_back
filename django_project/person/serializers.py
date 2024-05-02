from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')