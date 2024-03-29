from django.db import models
from django.contrib.postgres.fields import ArrayField


class Student(models.Model):
    ID = models.IntegerField(primary_key=True)
    PAPA = models.SmallIntegerField()
    PAPI = models.SmallIntegerField()
    PA = models.SmallIntegerField()
    PBM = models.SmallIntegerField()
    advance = models.SmallIntegerField()
    faculty = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    calls_done = models.BinaryField()
    current_applications = models.BinaryField()
    is_enrolled = models.BooleanField()
    date_banned_mobility = models.DateField(default='2000-01-01')
    is_banned_behave_un = models.BooleanField()
    admission = models.CharField(max_length=255)
    study_level = models.CharField(max_length=255)
    num_semesters = models.SmallIntegerField()
    contact_id = models.IntegerField()
