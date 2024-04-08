import json
import os
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from django_project.constants import Constants


class University(models.Model):

    id = models.BigAutoField(primary_key = True, auto_created = True)
    name = models.CharField(max_length=255)
    webpage = models.CharField(max_length=255)


    region_choices = [(choice['value'], _(choice['display'])) for choice in Constants.REGION_CHOICES]
    region = models.CharField(max_length=10, choices=region_choices)
    

    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    academic_offer = models.CharField(max_length=255)
    exchange_info = models.CharField(max_length=255)


    def __str__(self):
        return f'University: {self.name}'


class Call(models.Model):

    university_id = models.ForeignKey('University', on_delete=models.CASCADE)
    active = models.BooleanField()
    begin_date = models.DateField()
    deadline = models.DateField()
    min_advance = models.FloatField()
    min_papa = models.FloatField()

    format_choices = [(choice['value'], _(choice['display'])) for choice in Constants.FORMAT_CHOICES]
    format = models.CharField(max_length=10, choices=format_choices)

    study_level_choices = [(choice['value'], _(choice['display'])) for choice in Constants.STUDY_LEVEL_CHOICES]
    study_level = models.CharField(max_length=10, choices=study_level_choices)


    year = models.SmallIntegerField()

    semester_choices = [(choice['value'], _(choice['display'])) for choice in Constants.SEMESTER_CHOICES]
    semester = models.CharField(max_length=10, choices=semester_choices)

    language_choices = [(choice['value'], _(choice['display'])) for choice in Constants.LANGUAGE_CHOICES]
    language = models.CharField(max_length=10, choices=language_choices)

    description = models.TextField()
    available_slots = models.SmallIntegerField()
    note = models.TextField(blank=True, null=True)

    # Add 3 new fields only for testing in case 3 (need to create a new model that includes this).
    highest_papa_winner = models.FloatField(default=0.0)
    minimum_papa_winner = models.FloatField(default=0.0)
    selected = models.IntegerField(default=0)

    def __str__(self):
        return f'Call: university {self.university_id.name} during semester {self.semester} on year {self.year}'
