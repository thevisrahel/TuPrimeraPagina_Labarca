from django.db import models
from django.contrib.auth.models import User

class Viaje(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viajes', null=True)
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='viajes/', null=True, blank=True)
    
    def __str__(self):
        return f'Viaje: {self.destino}'