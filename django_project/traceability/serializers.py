from rest_framework import serializers
from .models import Traceability


class TraceabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Traceability
        fields = '__all__'
