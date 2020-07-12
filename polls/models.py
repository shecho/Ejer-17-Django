from django.db import models


class Clase(models.Model):
    id = models.CharField(max_length=200)
    fecha = models.DateTimeField('date published')


class Estudiante(models.Model):
    id_estudiante = models.ForeignKey(Clase, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)