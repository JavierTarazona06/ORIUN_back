from django.db import models
from data.constants import Constants
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    call = models.ForeignKey('call.Call', on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    semester_choices = [(choice['value'], _(choice['display'])) for choice in Constants.SEMESTER_CHOICES]
    semester = models.CharField(max_length=10, choices=semester_choices)
    is_extension = models.BooleanField()
    comment = models.TextField(null=True)
    state_documents_choices = [(choice['value'], _(choice['display'])) for choice in Constants.STATE_DOCS_CHOICES]
    state_documents = models.SmallIntegerField(default=0, choices=state_documents_choices)
    modified = models.BooleanField(default=False)
    approved = models.BooleanField(null=True)
    training_session = ArrayField(models.DateTimeField(), null=True)

    # Name of the base documents and name of the documents of each region
    name_docs = [
        'request_form', 'responsibility_form', 'data_processing_form', 'doc_id_student', 'grades_certificate'
    ]
    international_name_docs = [
        'motivation_letter', 'passport', 'language_certificate', 'economic_letter'
    ]
    national_name_docs = [
        'sigueme_form', 'payment_tuition', 'eps_certificate', 'economic_letter'
    ]

    def __str__(self):
        return f"Student {self.student.id} at call {self.call.id}."
