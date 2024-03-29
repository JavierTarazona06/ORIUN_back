from django.db import models
from django.contrib.postgres.fields import ArrayField


class Application(models.Model):
    call_id = models.ForeignKey('call.Call', on_delete=models.CASCADE)
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    doc_id_student = models.TextField()
    approved = models.BooleanField()
    is_extension = models.BooleanField()
    approve_documents = models.BooleanField()
    destination_faculty = models.TextField()
    destination_program = models.TextField()
    dest_contact_email = models.TextField()
    dest_contact_name = models.TextField()
    dest_contact_position = models.TextField()
    dest_contact_cellphone = models.TextField()
    starting_date = models.DateField()
    ending_date = models.DateField()
    info_courses = models.JSONField()
    diseases = models.TextField()
    medication = models.TextField()
    other_documents = models.JSONField()
    grades_certificate = models.TextField()
    training_session = ArrayField(models.DateTimeField())

    def __str__(self):
        return f"Application for {self.student_id.id} at {self.call_id.id}."
