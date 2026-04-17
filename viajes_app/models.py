from django.db import models

class Viaje(models.Model):
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.destino