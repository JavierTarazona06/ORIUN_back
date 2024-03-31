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
        ARTES = 'ARTES', _('Artes')
        CIENCIAS = 'CIENCIAS', _('Ciencias')
        AGRARIAS = 'AGRARIAS', _('Ciencias Agrarias')
        ECONOMICAS = 'ECONOMICAS', _('Ciencias Económicas')
        DERECHO_POLITICAS_SOCIALES = 'DERECHO_POLITICAS_SOCIALES', _('Derecho, Ciencias Políticas y Sociales')
        ENFERMERIA = 'ENFERMERIA', _('Enfermería')
        HUMANAS = 'HUMANAS', _('Ciencias Humanas')
        INGENIERIA = 'INGENIERIA', _('Ingeniería')
        MEDICINA = 'MEDICINA', _('Medicina')
        ODONTOLOGIA = 'ODNTOLOGIA', _('Odontología')
        VETERINARIA_ZOOTECNIA = 'VETERINARIA', _('Veterinaria y de Zootecnia')

    class Major(models.TextChoices):
        # faculty of arts
        ARQUITECTURA = 'ARQ', _('Arquitectura')
        ARTES_PLASTICAS = 'AP', _('Artes plásticas')
        CINE_TELEVISION = 'CT', _('Cine y Televisión')
        DISENO_GRAFICO = 'DG', _('Diseño Gráfico')
        DISENO_INDUSTRIAL = 'DI', _('Diseño Industrial')
        MUSICA = 'MUS', _('Música')
        MUSICA_INSTRUMENTAL = 'MUS_INST', _('Música Instrumental')
        # faculty of science
        BIOLOGIA = 'BIO', _('Biología')
        CIENCIAS_COMPUTACION = 'CC', _('Ciencias de la Computación')
        ESTADISTICA = 'EST', _('Estadística')
        FARMACIA = 'FAR', _('Farmacia')
        FISICA = 'FIS', _('Física')
        GEOLOGIA = 'GEOL', _('Geología')
        MATEMATICAS = 'MAT', _('Matemáticas')
        QUIMICA = 'QUI', _('Química')
        # faculty of agricultural sciences
        INGENIERIA_AGRONOMICA = 'IG', _('Ingeniería Agronómica')
        # faculty of economic sciences
        ADMINISTRACION_EMPRESAS = 'AE', _('Administración de Empresas')
        CONTADURIA = 'CON', _('Contaduría')
        ECONOMIA = 'ECO', _('Economía')
        # faculty of law, political  and social sciences
        CIENCIA_POLITICA = 'CP', _('Ciencia Política')
        DERECHO = 'DER', _('Derecho')
        # faculty of nursing
        ENFERMERIA = 'ENF', _('Enfermería')
        # faculty of humanities
        ANTROPOLOGIA = 'ANT', _('Antropología')
        ESTUDIOS_LITERARIOS = 'EST_LIT', _('Estudios Literarios')
        ESPANOL_FILOLOGIA_CLASICA = 'ESP_FIL_CLAS', _('Español y Filología Clásica')
        FILOSOFIA = 'FIL', _('Filosofía')
        GEOGRAFIA = 'GEOG', _('Geografía')
        HISTORIA = 'HIS', _('Historia')
        FILOLOGIA_IDIOMAS = 'FIL_IDI', _('Filología e Idiomas (Inglés, Alemán o Francés)')
        LINGUISTICA = 'LIN', _('Lingüística')
        PSICOLOGIA = 'PSI', _('Psicología')
        SOCIOLOGIA = 'SOC', _('Sociología')
        # faculty of engineering
        INGENIERIA_AGRICOLA = 'IA', _('Ingeniería Agrícola')
        INGENIERIA_CIVIL = 'IC', _('Ingeniería Civil')
        INGENIERIA_ELECTRICA = 'I_ELECTRI', _('Ingeniería Eléctrica')
        INGENIERIA_ELECTRONICA = 'I_ELECTRO', _('Ingeniería Electrónica')
        INGENIERIA_INDUSTRIAL = 'II', _('Ingeniería Industrial')
        INGENIERIA_MECANICA = 'I_MEC', _('Ingeniería Mecánica')
        INGENIERIA_MECATRONICA = 'I_MECAT', _('Ingeniería Mecatrónica')
        INGENIERIA_QUIMICA = 'IQ', _('Ingeniería Química')
        INGENIERIA_SISTEMAS_COMPUTACION = 'ISC', _('Ingeniería de Sistemas y Computación')
        # faculty of medicine
        FISIOTERAPIA = 'FISIO', _('Fisioterapia')
        FONOAUDIOLOGIA = 'FONO', _('Fonoaudiología')
        MEDICINA = 'MED', _('Medicina')
        NUTRICION_DIETETICA = 'NUTR', _('Nutrición y Dietética')
        TERAPIA_OCUPACIONAL = 'TER_OCUP', _('Terapia Ocupacional')
        #faculty of dentistry
        ODONTOLOGIA = 'ODO', _('Odontología')
        # faculty of veterinary medicine and zootechnics
        MEDICINA_VETERINARIA = 'MED_VET', _('Medicina Veterinaria')
        ZOOTECNIA = 'ZOO', _('Zootecnia')

    class Admission(models.TextChoices):
        REGULAR = 'REG', _('Regular')
        ESPECIAL = 'ESP', _('Especial')

    class StudyLevel(models.TextChoices):
        PREGRADO = 'PRE', _('Pregrado')
        POSGRADO = 'POS', _('Posgrado')
        DOCTORADO = 'DOC', _('Doctorado')

    PAPA = models.FloatField()
    PAPI = models.FloatField()
    PA = models.FloatField()
    PBM = models.SmallIntegerField()
    advance = models.FloatField()
    faculty = models.CharField(
        max_length=50,
        choices=Faculty.choices,
    )
    major = models.CharField(
        max_length=50,
        choices=Major.choices
    )
    calls_done = models.ManyToManyField('call.Call')
    # TODO: check how to add this: current_applications
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
