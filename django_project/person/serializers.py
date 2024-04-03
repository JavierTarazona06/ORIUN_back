from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    type_user = serializers.CharField(source='person.type_user')

    class Meta:
        model = Person
        fields = '__all__'
