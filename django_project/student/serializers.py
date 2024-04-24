from rest_framework import serializers
from .models import Student, ContactPerson
from django_project.constants import Constants


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
        return Constants.INFO_FACULTIES[headquarter][faculty][major]

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
