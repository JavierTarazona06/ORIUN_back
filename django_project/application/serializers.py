from call.models import Call
from .models import Application
from student.models import Student
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
        return obj.call.university_id.name

    def get_university_country(self, obj):
        return obj.call.university_id.country

    class Meta:
        model = Application
        fields = ['call', 'university_name', 'university_country', 'state_documents', 'approved']


class ApplicationComments(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()

    def get_comment_docs(self, obj):
        if obj.comment is None:
            return 'No hay comentarios con respecto a los documentos subidos.'
        return obj.comment

    class Meta:
        model = Application
        fields = ['comment']


class Applicants(serializers.ModelSerializer):
    year = serializers.IntegerField(required=False)
    semester = serializers.CharField(required=False)
    student_name = serializers.SerializerMethodField()
    student_major = serializers.SerializerMethodField()
    state_documents = serializers.SerializerMethodField()
    university_name = serializers.SerializerMethodField()
    university_country = serializers.SerializerMethodField()
    call = serializers.PrimaryKeyRelatedField(queryset=Call.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)


    def get_university_name(self, obj):
        return obj.call.university_id.name
    def get_student_name(self, obj):
        return obj.student.user.get_full_name()

    def get_university_country(self, obj):
        return obj.call.university_id.country

    def get_student_major(self, obj):
        return obj.student.get_major_display()

    def get_state_documents(self, obj):
        return obj.get_state_documents_display()

    class Meta:
        model = Application
        fields = ['call','student_id','university_name','university_country','year','semester','student_name','student_major', 'state_documents']

class ApplicationModifySerializer(serializers.ModelSerializer):
    call_id = serializers.PrimaryKeyRelatedField(queryset=Call.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    class Meta:
        model = Application
        fields = ['state_documents', 'call_id', 'student_id']

class StateSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    call_id = serializers.IntegerField()
    state = serializers.IntegerField()
    class Meta:
        fields = ('student_id', 'call_id', 'state')