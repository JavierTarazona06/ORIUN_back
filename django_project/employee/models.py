from django.db import models
from person.models import Person
from django.utils.translation import gettext_lazy as _


class Employee(Person):
    class Dependence(models.TextChoices):
        ORI = 'ORI', _('Oficina de Relaciones Interinstitucionales')
        DRE = 'DRE', _('Dirección de Relaciones Internacionales')

    dependency = models.CharField(max_length=3, choices=Dependence.choices)
