from django.db import models
from person.models import Person
from django.utils.translation import gettext_lazy as _
from django_project.constants import Constants


class Employee(Person):

    dependency_choices = [(choice['value'], _(choice['display'])) for choice in Constants.DEPENDENCE_CHOICES]
    dependency = models.CharField(max_length=3, choices=dependency_choices)

    def __str__(self):
        return f"Employee: {self.name} with ID {self.id}."
