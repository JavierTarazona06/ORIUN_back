from django.db import models
from django.contrib.auth.models import User
from data.constants import Constants
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    birth_date = models.DateField()

    type_document_choices = [(choice['value'], _(choice['display'])) for choice in Constants.TYPE_DOC_CHOICES]
    type_document = models.CharField(max_length=10, choices=type_document_choices)

    sex_choices = [(choice['value'], _(choice['display'])) for choice in Constants.SEX_CHOICES]
    sex = models.CharField(max_length=2, choices=sex_choices)

    ethnicity_choices = [(choice['value'], _(choice['display'])) for choice in Constants.ETHNICITY_CHOICES]
    ethnicity = models.CharField(max_length=3, choices=ethnicity_choices)

    headquarter_choices = [(choice['value'], _(choice['display'])) for choice in Constants.HEADQUARTER_CHOICES]
    headquarter = models.CharField(max_length=3, choices=headquarter_choices)

    class Meta:
        abstract = True
