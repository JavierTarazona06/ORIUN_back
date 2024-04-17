from rest_framework import serializers
from .models import Call, University
from django_project.constants_dict_front import constants_dict_front

class CallSerializerOpen(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university_id.name')
    country = serializers.CharField(source='university_id.country')
    language = serializers.SerializerMethodField()
    deadline = serializers.DateField(format='%Y-%m-%d')
    region =  serializers.SerializerMethodField(source = 'university_id.region')

    def get_language(self, obj):
        language_value = obj.language
        return constants_dict_front.get("language", {}).get(str(language_value), language_value)

    def get_region(self, obj):
        university = obj.university_id
        if university:
            return constants_dict_front.get("region", {}).get(str(university.region), university.region)
        return None

    class Meta:
        model = Call
        fields = ('id','university_name', 'country', 'language', 'deadline','region')

class CallSerializerClosed(CallSerializerOpen):
    class Meta(CallSerializerOpen.Meta):
        fields = CallSerializerOpen.Meta.fields + ('minimum_papa_winner',)


class CallDetailsSerializerOpenStudent(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university_id.name')
    country = serializers.CharField(source='university_id.country')
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
    format = serializers.CharField(source="get_format_display")
    study_level = serializers.CharField(source="get_study_level_display")
    language = serializers.CharField(source="get_language_display")
    class Meta:
        model = Call
        fields = '__all__'

class CallSerializerPost(serializers.ModelSerializer):
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

class CallForUniSerializer(serializers.ModelSerializer):
    university_id = UniversitySerializer()
    format = serializers.CharField(source="get_format_display")
    study_level = serializers.CharField(source="get_study_level_display")
    language = serializers.CharField(source="get_language_display")
    class Meta:
        model = Call
        fields = '__all__'
