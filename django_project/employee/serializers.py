from rest_framework import serializers
from .models import Employee
from person.serializers import UserSerializerShort


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializerGeneral(serializers.ModelSerializer):
    user = UserSerializerShort()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeGetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Employee
        lista = []
        for field in Employee._meta.fields:
            if not (field.name == 'user'):
                lista.append(field.name)
        fields = ['email', 'first_name', 'last_name'] + lista
