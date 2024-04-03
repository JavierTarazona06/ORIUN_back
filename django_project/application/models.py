from django.db import models
from django.contrib.postgres.fields import ArrayField


class Application(models.Model):
    call_id = models.ForeignKey('call.Call', on_delete=models.CASCADE)
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    doc_id_student = models.CharField(max_length=255)
    approved = models.BooleanField(null=True)
    is_extension = models.BooleanField()
    comment_approved = models.TextField(null=True)
    approve_documents = models.BooleanField()
    comment_docs = models.TextField(null=True)
    destination_faculty = models.CharField(max_length=50)
    destination_program = models.CharField(max_length=50)
    dest_contact_email = models.CharField(max_length=50)
    dest_contact_name = models.CharField(max_length=50)
    dest_contact_position = models.CharField(max_length=50)
    dest_contact_cellphone = models.CharField(max_length=50)
    starting_date = models.DateField()
    ending_date = models.DateField()
    info_courses = models.JSONField()
    diseases = models.TextField()
    medication = models.TextField()
    other_documents = models.JSONField()
    grades_certificate = models.CharField(max_length=255)
    training_session = ArrayField(models.DateTimeField())

    def __str__(self):
        return f"Application: student {self.student_id.id} at call {self.call_id}."
