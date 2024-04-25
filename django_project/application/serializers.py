from .models import Application
from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validated_data):
        return Application.objects.create(**validated_data)


class ApplicationDetailSerializer(serializers.ModelSerializer):
    university_name = serializers.SerializerMethodField()
    university_country = serializers.SerializerMethodField()

    def get_university_name(self, obj):
        return obj.call.university.name

    def get_university_country(self, obj):
        return obj.call.university.country

    class Meta:
        model = Application
        fields = ['call', 'university_name', 'university_country', 'approve_documents', 'approved']


class ApplicationComments(serializers.ModelSerializer):
    comment_docs = serializers.SerializerMethodField()

    def get_comment_docs(self, obj):
        if obj.comment_docs is None:
            return 'No hay comentarios con respecto a los documentos subidos.'
        return obj.comment_docs

    class Meta:
        model = Application
        fields = ['comment_docs']
