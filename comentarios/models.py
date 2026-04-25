from django.db import models                                     # Importa el sistema de modelos de Django
from django.contrib.auth.models import User                      # Modelo de usuario por defecto
from viajes_app.models import Viaje                              # Modelo de viajes


class Comentario(models.Model):                                  # Modelo para comentarios (incluye respuestas tipo hilo)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que hizo el comentario

    viaje = models.ForeignKey(
        Viaje,
        on_delete=models.CASCADE,
        related_name='comentarios'                               # Permite acceder con viaje.comentarios.all()
    )

    texto = models.TextField()                                   # Contenido del comentario

    creado = models.DateTimeField(auto_now_add=True)             # Fecha de creación automática

    padre = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='respuestas'                                # Permite acceder a respuestas con comentario.respuestas.all()
    )                                                            # Relación para comentarios anidados (respuestas)

    def __str__(self):
        return f"{self.usuario.username} - {self.texto[:30]}"     # Representación corta (usuario + parte del texto)


class Notificacion(models.Model):                                # Modelo para notificaciones relacionadas a comentarios

    TIPOS = [
        ('comentario', 'Comentario en tu viaje'),                # Tipo: alguien comentó tu viaje
        ('respuesta', 'Respuesta a tu comentario'),              # Tipo: alguien respondió tu comentario
    ]

    destinatario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notificaciones'                            # Acceso: user.notificaciones.all()
    )                                                            # Usuario que recibe la notificación

    remitente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notificaciones_enviadas'                   # Acceso: user.notificaciones_enviadas.all()
    )                                                            # Usuario que genera la acción

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS                                            # Limita valores posibles a los definidos en TIPOS
    )

    comentario = models.ForeignKey(
        Comentario,
        on_delete=models.CASCADE,
        related_name='notificaciones'                            # Acceso: comentario.notificaciones.all()
    )                                                            # Comentario asociado a la notificación

    leida = models.BooleanField(default=False)                   # Indica si el usuario ya vio la notificación

    creada = models.DateTimeField(auto_now_add=True)             # Fecha de creación automática

    def __str__(self):
        return f"{self.tipo} de {self.remitente} → {self.destinatario}"  # Representación descriptiva