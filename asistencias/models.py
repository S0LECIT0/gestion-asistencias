from django.db import models

class Asistencia(models.Model):
    tipo_documento = models.CharField(max_length=2)
    documento = models.CharField(max_length=11)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=10)
    fecha = models.DateField()
    asistio = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres
    