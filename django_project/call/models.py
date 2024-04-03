from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class University(models.Model):
    # TODO: add the other enums for University
    class Region(models.TextChoices):
        NORTE_AMERICA = "NA", _("Norte América")

    class Language(models.TextChoices):
        ENGLISH = "en", _("Inglés")

    name = models.CharField(max_length=50)
    webpage = models.CharField(max_length=255)
    region = models.CharField(
        max_length=2,
        choices=Region.choices
    )
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    language = ArrayField(models.CharField(max_length=2, choices=Language.choices))
    academic_offer = models.CharField(max_length=255)
    exchange_info = models.CharField(max_length=255)

    def __str__(self):
        return f'University: {self.name}'


class Call(models.Model):
    # TODO: add the other enums for Call
    class Format(models.TextChoices):
        PRESENCIAL = "P", _("Presencial")

    class StudyLevel(models.TextChoices):
        PREGRADO = "P", _("Pregrado")

    class Semester(models.IntegerChoices):
        FIRST = 1
        SECOND = 2

    university_id = models.ForeignKey('University', on_delete=models.CASCADE)
    active = models.BooleanField()
    begin_date = models.DateField()
    deadline = models.DateField()
    min_advance = models.FloatField()
    min_papa = models.FloatField()
    format = models.CharField(
        max_length=1,
        choices=Format.choices
    )
    study_level = models.CharField(
        max_length=1,
        choices=StudyLevel.choices
    )
    year = models.SmallIntegerField()
    semester = models.CharField(choices=Semester.choices)
    description = models.TextField()
    available_slots = models.SmallIntegerField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'University ID: {self.university_id}'
