from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class TypeDocument(models.TextChoices):
        CEDULA_CIUDADANIA = 'CC', _('Cédula de ciudadanía')
        CEDULA_EXTRANJERIA = 'CE', _('Cédula de extranjería')
        PASAPORTE = 'PA', _('Pasaporte')

    class Sex(models.TextChoices):
        MUJER = 'M', _('Mujer')
        HOMBRE = 'H', _('Hombre')

    class Ethnicity(models.TextChoices):
        INDIGENA = 'I', _('Indígena')
        AFROCOLOMBIANA = 'A', _('Afrocolombiana')
        ROM_GITANA = 'RG', _('Rom o gitana')
        NINGUNA = 'N', _('Ninguna')

    class Headquarter(models.TextChoices):
        AMAZONIA = 'A', _('Amazonia'),
        CARIBE = 'C', _('Caribe'),
        BOGOTA = 'B', _('Bogotá'),
        MANIZALES = 'MA', _('Manizales'),
        MEDELLIN = 'ME', _('Medellin'),
        ORINOQUIA = 'O', _('Orinoquía'),
        PALMIRA = 'P', _('Palmira'),
        TUMACO = 'T', _('Tumaco')
        LA_PAZ = 'LP', _('La Paz')

    type_document = models.CharField(
        max_length=2,
        choices=TypeDocument.choices
    )
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth = models.DateField()
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices
    )
    birth_place = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.TextField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    ethnicity = models.CharField(
        max_length=2,
        choices=Ethnicity.choices,
        default=Ethnicity.NINGUNA
    )
    headquarter = models.CharField(
        max_length=2,
        choices=Headquarter.choices,
        default=Headquarter.BOGOTA
    )

    class Meta:
        abstract = True
