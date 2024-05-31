from rest_framework import serializers
from .models import Call, University
from data.constants import Constants


class CallSerializerOpen(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name')
    country = serializers.CharField(source='university.country')
    language =  serializers.SerializerMethodField()
    deadline = serializers.DateField(format='%Y-%m-%d')
    region = serializers.SerializerMethodField()
    flag_image_url = serializers.URLField(source='university.flag_image_url')
    def get_language(self, obj):
        return obj.get_language_display()

    def get_region(self,obj):
        return obj.university.get_region_display()

    class Meta:
        model = Call
        fields = ('id','university_name', 'country', 'language', 'deadline','region','flag_image_url')

class CallSerializerClosed(CallSerializerOpen):

    class Meta(CallSerializerOpen.Meta):
        fields = CallSerializerOpen.Meta.fields + ('minimum_papa_winner',)


class CallDetailsSerializerOpenStudent(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name')
    country = serializers.CharField(source='university.country')
    language =  serializers.SerializerMethodField()
    deadline = serializers.DateField(format='%Y-%m-%d')
    min_advance = serializers.FloatField()
    min_papa = serializers.FloatField()
    format = serializers.SerializerMethodField()
    year = serializers.IntegerField()
    semester = serializers.IntegerField()
    description = serializers.CharField(allow_null=True)
    available_slots = serializers.IntegerField()
    note = serializers.CharField(allow_null=True)
    flag_image_url = serializers.URLField(source='university.flag_image_url')

    def get_language(self, obj):
        return obj.get_language_display()

    def get_format(self,obj):
        return obj.get_format_display()

    class Meta:
        model = Call
        fields = (
        'university_name', 'country', 'language', 'deadline', 'min_advance', 'min_papa', 'format', 'year', 'semester',
        'description', 'available_slots', 'note', 'flag_image_url')


class CallDetailsSerializerClosedStudent(CallDetailsSerializerOpenStudent):
    minimum_papa_winner = serializers.CharField()
    highest_papa_winner = serializers.CharField()
    selected = serializers.IntegerField()

    class Meta(CallDetailsSerializerOpenStudent.Meta):
        fields = CallDetailsSerializerOpenStudent.Meta.fields + (
        'minimum_papa_winner', 'highest_papa_winner', 'selected','flag_image_url')


class CallSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'


class CallSerializer(serializers.ModelSerializer):
    format = serializers.CharField(source="get_format_display")
    study_level = serializers.CharField(source="get_study_level_display")
    language = serializers.CharField(source="get_language_display")

    class Meta:
        model = Call
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    region = serializers.CharField(source="get_region_display")

    class Meta:
        model = University
        fields = '__all__'


class UniversitySerializerPost(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

