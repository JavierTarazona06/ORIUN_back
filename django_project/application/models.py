from django.db import models
from django_project.constants import Constants
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class InternationalApplication(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    motivation_letter = models.CharField(max_length=255)
    passport = models.CharField(max_length=255)
    language_certificate = models.CharField(max_length=255)
    economic_letter = models.CharField(max_length=255)


class NationalApplication(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    sigueme_form = models.CharField(max_length=255)
    payment_tuition = models.CharField(max_length=255)
    eps_certificate = models.CharField(max_length=255)
    economic_letter = models.CharField(max_length=255)


class Application(models.Model):
    call = models.ForeignKey('call.Call', on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    semester_choices = [(choice['value'], _(choice['display'])) for choice in Constants.SEMESTER_CHOICES]
    semester = models.CharField(max_length=10, choices=semester_choices, default=Constants.SEMESTER_CHOICES[0])
    is_extension = models.BooleanField()
    comment_docs = models.TextField(null=True)
    approve_documents = models.BooleanField(null=True)
    comment_approved = models.TextField(null=True)
    approved = models.BooleanField(null=True)
    training_session = ArrayField(models.DateTimeField())

    # Link documents
    request_form = models.CharField(max_length=255)
    responsibility_form = models.CharField(max_length=255)
    data_processing_form = models.CharField(max_length=255)
    doc_id_student = models.CharField(max_length=255)
    grades_certificate = models.CharField(max_length=255)
    other_documents = models.JSONField(null=True)

    def __str__(self):
        return f"Student {self.student.id} at call {self.call.id}."
