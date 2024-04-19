from datetime import date
from django.db import models
from person.models import Person
from django_project.constants import Constants
from django.utils.translation import gettext_lazy as _


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
    PAPI = models.FloatField()
    PA = models.FloatField()
    PBM = models.SmallIntegerField()
    advance = models.FloatField()
    calls_done = models.ManyToManyField('call.Call')
    is_enrolled = models.BooleanField()
    date_banned_mobility = models.DateField(default=date(2000, 1, 1))
    is_banned_behave_un = models.BooleanField()
    num_semesters = models.SmallIntegerField()
    # TODO: change to contact_person
    contact_id = models.ForeignKey(ContactPerson, on_delete=models.SET_NULL, null=True)
    diseases = models.TextField(null=True, blank=True)
    medication = models.TextField(null=True, blank=True)

    faculty_choices = [(choice['value'], _(choice['display'])) for choice in Constants.FACULTY_CHOICES]
    faculty = models.CharField(max_length=50, choices=faculty_choices)

    major_choices = [(choice['value'], _(choice['display'])) for choice in Constants.MAJOR_CHOICES]
    major = models.CharField(max_length=50, choices=major_choices)

    admission_choices = [(choice['value'], _(choice['display'])) for choice in Constants.ADMISSION_CHOICES]
    admission = models.CharField(max_length=10, choices=admission_choices)

    study_level_choices = [(choice['value'], _(choice['display'])) for choice in Constants.STUDY_LEVEL_CHOICES]
    study_level = models.CharField(max_length=10, choices=study_level_choices)

    def __str__(self):
        return f'Student: {self.name} with ID {self.id}.'
