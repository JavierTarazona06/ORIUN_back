from rest_framework import serializers
from .models import Student, ContactPerson


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'


class StudentApplicationSerializer(serializers.ModelSerializer):
    contact_id = ContactPersonSerializer(required=False)

    class Meta:
        model = Student
        fields = ['contact_id', 'diseases', 'medication']

    def update(self, instance, validated_data):
        instance.diseases = validated_data.get('diseases', instance.diseases)
        instance.medication = validated_data.get('medication', instance.medication)

        contact_person_data = validated_data.get('contact_id')
        if contact_person_data:
            if instance.contact_id:
                ContactPerson.objects.filter(id=instance.contact_id.id).update(**contact_person_data)
            else:
                contact_person = ContactPerson.objects.create(**contact_person_data)
                instance.contact_id = contact_person

        instance.save()
        return instance
