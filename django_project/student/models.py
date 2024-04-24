from django.db import models
from person.models import Person
from django.utils.translation import gettext_lazy as _
from django_project.constants import Constants
from datetime import date

class ContactPerson(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    relationship = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=20)

    def __str__(self):
        return f'Contact {self.name}, {self.last_name}'


class Student(Person):

    PAPA = models.FloatField()
    PBM = models.SmallIntegerField()
    advance = models.FloatField()

    faculty_choices = [(choice['value'], _(choice['display'])) for choice in Constants.FACULTY_CHOICES]
    faculty = models.CharField(max_length=50, choices=faculty_choices)

    major_choices = [(choice['value'], _(choice['display'])) for choice in Constants.MAJOR_CHOICES]
    major = models.CharField(max_length=50, choices=major_choices)


    calls_done = models.ManyToManyField('call.Call')
    is_enrolled = models.BooleanField()
    date_banned_mobility = models.DateField(default=date(2000, 1, 1))

    admission_choices = [(choice['value'], _(choice['display'])) for choice in Constants.ADMISSION_CHOICES]
    admission = models.CharField(max_length=10, choices=admission_choices, default=admission_choices[0])
    # admission_choices[0] debe ser "Regular"

    study_level_choices = [(choice['value'], _(choice['display'])) for choice in Constants.STUDY_LEVEL_CHOICES]
    study_level = models.CharField(max_length=10, choices=study_level_choices)

    num_semesters = models.SmallIntegerField()
    contact_id = models.ForeignKey(ContactPerson, on_delete=models.CASCADE, null=True)

    certificates = ['certificate_grades', 'certificate_student', 'payment_receipt']

    def __str__(self):
        return f'Student: {self.name} with ID {self.id}.'
