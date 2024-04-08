# Generated by Django 5.0.3 on 2024-04-08 17:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('call', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('relationship', models.CharField(max_length=50)),
                ('cellphone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_user', models.CharField(choices=[('E', 'Estudiante'), ('T', 'Trabajador')], max_length=2)),
                ('type_document', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('PA', 'Pasaporte')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('birth_place', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('ethnicity', models.CharField(choices=[('IN', 'Indígena'), ('AF', 'Afrocolombiana'), ('RG', 'Rom o gitana'), ('NA', 'Ninguna')], default=('NA', 'Ninguna'), max_length=2)),
                ('headquarter', models.CharField(choices=[('BO', 'Bogotá'), ('AM', 'Amazonia'), ('CA', 'Caribe'), ('MA', 'Manizales'), ('ME', 'Medellín'), ('OR', 'Orinoquia'), ('PA', 'Palmira'), ('TU', 'Tumaco'), ('LP', 'La Paz')], default=('BO', 'Bogotá'), max_length=2)),
                ('PAPA', models.FloatField()),
                ('PAPI', models.FloatField()),
                ('PA', models.FloatField()),
                ('PBM', models.SmallIntegerField()),
                ('advance', models.FloatField()),
                ('faculty', models.CharField(choices=[('Ciencias Agrarias', 'Facultad de Ciencias Agrarias'), ('Ciencias Económicas', 'Facultad de Ciencias Económicas'), ('Ciencias Humanas', 'Facultad de Ciencias Humanas'), (' Ciencias', 'Facultad de Ciencias'), ('Ciencias Agropecuarias', 'Facultad de Ciencias Agropecuarias'), ('Derecho, Ciencias Políticas y Sociales', 'Facultad de Derecho, Ciencias Políticas y Sociales'), ('Ingeniería', 'Facultad de Ingeniería'), ('Medicina', 'Facultad de Medicina'), ('Minas', 'Facultad de Minas'), ('Odontología', 'Facultad de Odontología'), ('Enfermería', 'Facultad de Enfermería'), ('Arquitectura', 'Facultad de Arquitectura'), ('Artes', 'Facultad de Artes'), ('Ciencias Administrativas', 'Facultad de Ciencias Administrativas')], max_length=50)),
                ('major', models.CharField(choices=[('ISCO', 'Ingeniería de Sistemas y Computación'), ('ISIN', 'Ingeniería de Sistemas e Informática'), ('ICIV', 'Ingeniería Civil'), ('IIND', 'Ingeniería Industrial'), ('IELO', 'Ingeniería Electrónica'), ('IELE', 'Ingeniería Eléctrica'), ('IMEC', 'Ingeniería Mecánica'), ('IMET', 'Ingeniería Mecatrónica'), ('IQUI', 'Ingeniería Química'), ('IAGR', 'Ingeniería Agrícola'), ('IAIN', 'Ingeniería Agroindustrial'), ('IAGN', 'Ingeniería Agronómica'), ('IGEO', 'Ingeniería Geológica'), ('IFOR', 'Ingeniería Forestal'), ('IMIN', 'Ingeniería de Minas y Metalurgia'), ('IPET', 'Ingeniería de Petróleos'), ('IADM', 'Ingeniería Administrativa'), ('ICON', 'Ingeniería de Control'), ('IAMB', 'Ingeniería Ambiental'), ('ECON', 'Economía'), ('ADME', 'Administración de Empresas'), ('CONT', 'Contaduría Pública'), ('DERE', 'Derecho'), ('MEDI', 'Medicina'), ('ODON', 'Odontología'), ('ENFE', 'Enfermería'), ('PSIC', 'Psicología'), ('ARQI', 'Arquitectura'), ('BIOL', 'Biología'), ('QUIM', 'Química'), ('FISI', 'Física'), ('MATE', 'Matemáticas'), ('ESTA', 'Estadística'), ('GEOL', 'Geología'), ('GEOG', 'Geografía'), ('SOCI', 'Sociología'), ('TRAB', 'Trabajo Social'), ('ANTR', 'Antropología'), ('HIST', 'Historia'), ('LING', 'Lingüística'), ('LITE', 'Literatura'), ('COSO', 'Comunicación Social'), ('FILO', 'Filosofía'), ('MUSI', 'Música'), ('MUIN', 'Música Instrumental'), ('DIND', 'Diseño Industrial'), ('BMAR', 'Biología Marina'), ('VETE', 'Medicina Veterinaria'), ('ZOOT', 'Zootecnia'), ('ARTE', 'Artes Plásticas'), ('CPOL', 'Ciencias Política'), ('CCOM', 'Ciencias de la Computación'), ('CITE', 'Cine y Televisión'), ('DGRA', 'Diseño Gráfico'), ('EFCL', 'Español y Filología Clásica'), ('FARM', 'Farmacia'), ('FIAL', 'Filología e Idiomas: Alemán'), ('FIFR', 'Filología e Idiomas: Francés'), ('FIIN', 'Filología e Idiomas: Inglés'), ('FISO', 'Fisioterapia'), ('NUDI', 'Nutrición y Dietética'), ('GECC', 'Gestión Cultural y Comunicativa'), ('ADSI', 'Administración de Sistemas Informáticos '), ('CONS', 'Construcción')], max_length=50)),
                ('is_enrolled', models.BooleanField()),
                ('date_banned_mobility', models.DateField(default='2000-01-01')),
                ('is_banned_behave_un', models.BooleanField()),
                ('admission', models.CharField(choices=[('REGUL', 'Regular'), ('PAES', 'PAES'), ('PEAMA', 'PEAMA')], default=('REGUL', 'Regular'), max_length=5)),
                ('study_level', models.CharField(choices=[('PRE', 'Pregrado'), ('POS', 'Postgrado'), ('DOC', 'Doctorado')], max_length=3)),
                ('num_semesters', models.SmallIntegerField()),
                ('calls_done', models.ManyToManyField(to='call.call')),
                ('contact_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.contactperson')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
