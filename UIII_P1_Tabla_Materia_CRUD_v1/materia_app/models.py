from django.db import models
class Materia (models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre