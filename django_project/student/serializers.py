from rest_framework import serializers
from .models import Student, ContactPerson
from data.constants import Constants
from .models import Student
from person.serializers import UserSerializerShort


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'


class StudentApplicationSerializer(serializers.ModelSerializer):
    contact_person = ContactPersonSerializer(required=False)
    info_coordinator = serializers.SerializerMethodField(read_only=True)

    def get_info_coordinator(self, obj):
        headquarter = obj.get_headquarter_display()
        faculty = obj.get_faculty_display()
        major = obj.get_major_display()
        try:
            return Constants.INFO_FACULTIES[headquarter][faculty][major]
        except KeyError:
            no_data = {
                "Coordinador Curricular": 'Desconocido',
                "Teléfono Coordinador": "Desconocido",
                "Correo Coordinador": "Desconocido",
                "Correo Coordinación Curricular": "Desconocido"
            }
            return no_data

    class Meta:
        model = Student
        fields = ['contact_person', 'diseases', 'medication', 'info_coordinator']

    def update(self, instance, validated_data):
        instance.diseases = validated_data.get('diseases', instance.diseases)
        instance.medication = validated_data.get('medication', instance.medication)

        contact_person_data = validated_data.get('contact_person')
        if contact_person_data:
            if instance.contact_person:
                ContactPerson.objects.filter(id=instance.contact_person.id).update(**contact_person_data)
            else:
                contact_person = ContactPerson.objects.create(**contact_person_data)
                instance.contact_person = contact_person

        instance.save()
        return instance


class StudentSerializerGeneral(serializers.ModelSerializer):
    user = UserSerializerShort()

    class Meta:
        model = Student
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentGetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Student
        lista = []
        for field in Student._meta.fields:
            if not (field.name == 'user' or field.name == 'contact_person'):
                lista.append(field.name)
        fields = ['email', 'first_name', 'last_name'] + lista
