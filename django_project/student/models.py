from django.db import models
from person.models import Person
from django.utils.translation import gettext_lazy as _


class ContactPerson(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    relationship = models.CharField(max_length=50)
    cellphone = models.IntegerField()

    def __str__(self):
        return f'Contact {self.name}, {self.last_name}'


class Student(Person):

    # TODO: add the other enums for Student
    class Faculty(models.TextChoices):
        AGRARIAS = 'AGRARIAS', _('Ciencias Agrarias')

    class Major(models.TextChoices):
        SISTEMAS = 'ISC', _('Ingeniería de Sistemas y Computación')

    class Admission(models.TextChoices):
        REGULAR = 'REG', _('Regular')

    class StudyLevel(models.TextChoices):
        PREGRADO = 'PRE', _('Pregrado')

    PAPA = models.FloatField()
    PAPI = models.FloatField()
    PA = models.FloatField()
    PBM = models.SmallIntegerField()
    advance = models.FloatField()
    faculty = models.CharField(
        max_length=10,
        choices=Faculty.choices,
    )
    major = models.CharField(
        max_length=5,
        choices=Major.choices
    )
    calls_done = models.ManyToManyField('call.Call')
    is_enrolled = models.BooleanField()
    date_banned_mobility = models.DateField(default='2000-01-01')
    is_banned_behave_un = models.BooleanField()
    admission = models.CharField(
        max_length=3,
        choices=Admission.choices,
        default=Admission.REGULAR,
    )
    study_level = models.CharField(
        max_length=3,
        choices=StudyLevel.choices
    )
    num_semesters = models.SmallIntegerField()
    contact_id = models.ForeignKey(ContactPerson, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Student: {self.name} with ID {self.id}.'
