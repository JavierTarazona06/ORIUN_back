from django.db import models


class Call(models.Model):
    ID = models.IntegerField(primary_key=True)
    university_id = models.IntegerField()
    active = models.BooleanField()
    begin_date = models.DateField()
    deadline = models.DateField()
    min_advance = models.SmallIntegerField()
    min_papa = models.SmallIntegerField()
    format = models.CharField(max_length=100)
    study_level = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    semester = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    available_slots = models.SmallIntegerField()
    note = models.TextField(blank=True, null=True)