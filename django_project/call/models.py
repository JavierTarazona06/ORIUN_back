from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class University(models.Model):

    class Region(models.TextChoices):
        NORTE_AMERICA = "NA", _("Norte América")
        CENTRO_AMERICA = "CA", _("Centro América")
        SUR_AMERICA = "SA", _("Sur América")
        EUROPA = "EU", _("Europa")
        ASIA = "AS", _("Asia")
        AFRICA = "AF", _("África")
        OCEANIA = "OC", _("Oceanía")
        ANTARTIDA = "AN", _("Antártida")

    class Language(models.TextChoices):
        ENGLISH = "en", _("Inglés")
        SPANISH = "es", _("Español")
        FRENCH = "fr", _("Francés")
        GERMAN = "de", _("Alemán")
        ITALIAN = "it", _("Italiano")
        PORTUGUESE = "pt", _("Portugués")
        CHINESE = "zh", _("Chino")
        JAPANESE = "ja", _("Japonés")
        KOREAN = "ko", _("Coreano")
        ARABIC = "ar", _("Árabe")
        RUSSIAN = "ru", _("Ruso")
        HINDI = "hi", _("Hindi")


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

    class Format(models.TextChoices):
        PRESENCIAL = "P", _("Presencial")
        VIRTUAL = 'V', _('Virtual')

    class StudyLevel(models.TextChoices):
        PREGRADO = 'PRE', _('Pregrado')
        POSGRADO = 'POS', _('Posgrado')
        DOCTORADO = 'DOC', _('Doctorado')

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
        max_length=10,
        choices=StudyLevel.choices
    )
    year = models.SmallIntegerField()
    semester = models.CharField(
        max_length=10,
        choices=Semester.choices
    )
    description = models.TextField()
    available_slots = models.SmallIntegerField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Call: university {self.university_id.name} during semester {self.semester} on year {self.year}'
