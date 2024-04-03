from rest_framework import serializers
from .models import University, Call

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'
