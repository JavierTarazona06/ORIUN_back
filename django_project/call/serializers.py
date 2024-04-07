from rest_framework import serializers
from .models import Call, University

class CallSerializerOpen(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university_id.name')
    country = serializers.CharField(source='university_id.country')
    language = serializers.ListField(child=serializers.CharField(), source='university_id.language')
    deadline = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Call
        fields = ('university_name', 'country', 'language', 'deadline')

class CallSerializerClosed(CallSerializerOpen):
    class Meta(CallSerializerOpen.Meta):
        fields = CallSerializerOpen.Meta.fields + ('minimum_papa_winner',)

