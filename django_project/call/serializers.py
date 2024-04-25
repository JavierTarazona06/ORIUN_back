from rest_framework import serializers
from .models import Call, University
from data.constants import Constants

class CallSerializerOpen(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name')
    country = serializers.CharField(source='university.country')
    language = serializers.CharField()
    deadline = serializers.DateField(format='%Y-%m-%d')


    class Meta:
        model = Call
        fields = ('id','university_name', 'country', 'language', 'deadline')

class CallSerializerClosed(CallSerializerOpen):
    class Meta(CallSerializerOpen.Meta):
        fields = CallSerializerOpen.Meta.fields + ('minimum_papa_winner',)


class CallDetailsSerializerOpenStudent(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name')
    country = serializers.CharField(source='university.country')
    #language = serializers.ChoiceField(choices=Call.language_choices)
    deadline = serializers.DateField(format='%Y-%m-%d')
    min_advance = serializers.FloatField()
    min_papa = serializers.FloatField()
    format = serializers.CharField()
    year = serializers.IntegerField()
    semester = serializers.IntegerField()
    description = serializers.CharField(allow_null=True)
    available_slots = serializers.IntegerField()
    note = serializers.CharField(allow_null=True)

    class Meta:
        model = Call
        fields = ('university_name', 'country', 'language', 'deadline', 'min_advance', 'min_papa', 'format', 'year', 'semester', 'description', 'available_slots', 'note')


class CallDetailsSerializerClosedStudent(CallDetailsSerializerOpenStudent):
    minimum_papa_winner = serializers.CharField()
    highest_papa_winner = serializers.CharField()
    selected = serializers.IntegerField()

    class Meta(CallDetailsSerializerOpenStudent.Meta):
        fields = CallDetailsSerializerOpenStudent.Meta.fields + ('minimum_papa_winner', 'highest_papa_winner', 'selected')


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

