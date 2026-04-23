from django.db import models
from django.contrib.auth.models import User
from viajes_app.models import Viaje

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')

    def __str__(self):
        return f"{self.usuario.username} - {self.texto[:30]}"