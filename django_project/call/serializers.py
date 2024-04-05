# serializers.py

from rest_framework import serializers
from .models import Call, University

class CallSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university_id.name')
    country = serializers.CharField(source='university_id.country')
    language = serializers.ListField(child=serializers.CharField(), source='university_id.language')
    deadline = serializers.DateField()

    class Meta:
        model = Call
        fields = ('university_name', 'country', 'language', 'deadline')
