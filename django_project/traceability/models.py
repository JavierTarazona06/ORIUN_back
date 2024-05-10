from django.db import models
from django.contrib.auth.models import User


class Traceability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    view = models.CharField(max_length=100)
    given_data = models.TextField()


# Crear tabla en la base de datos con:
# ¿Fecha, hora, quien y que hizo (modifico, creo, miro)?
#
# Ej: ¿Cuántas personas han ingresado y quienes?
