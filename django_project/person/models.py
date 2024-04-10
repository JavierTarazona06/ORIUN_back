import os
import json

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django_project.constants import Constants

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    type_user_choices = [(choice['value'], _(choice['display'])) for choice in Constants.TYPE_USER_CHOICES]
    type_user = models.CharField(max_length=10, choices=type_user_choices)

    type_document_choices = [(choice['value'], _(choice['display'])) for choice in Constants.TYPE_DOC_CHOICES]
    type_document = models.CharField(max_length=10, choices=type_document_choices)

    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    birth = models.DateField()

    sex_choices = [(choice['value'], _(choice['display'])) for choice in Constants.SEX_CHOICES]
    sex = models.CharField(max_length=2, choices=sex_choices)

    birth_place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    ethnicity_choices = [(choice['value'], _(choice['display'])) for choice in Constants.ETHNICITY_CHOICES]
    ethnicity = models.CharField(max_length=3, choices=ethnicity_choices, default=ethnicity_choices[-1])
    # ethnicity_choices[-1] debe ser "Ninguna"

    headquarter_choices = [(choice['value'], _(choice['display'])) for choice in Constants.HEADQUARTER_CHOICES]
    headquarter = models.CharField(max_length=3, choices=headquarter_choices, default=headquarter_choices[0])
    # ethnicity_choices[0] debe ser "Bogotá"

    class Meta:
        abstract = True
