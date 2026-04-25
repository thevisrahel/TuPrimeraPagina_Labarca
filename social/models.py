from django.db import models                                               # Módulo base para definir modelos de BD
from django.contrib.auth.models import User                                # Modelo de usuario integrado de Django


class Seguimiento(models.Model):                                           # Modelo que representa una relación de seguimiento
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='siguiendo')  # Usuario que sigue
    seguido  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguidores') # Usuario que es seguido
    fecha    = models.DateTimeField(auto_now_add=True)                     # Fecha en que se creó el seguimiento

    class Meta:
        unique_together    = ('seguidor', 'seguido')                       # Evita que un usuario siga dos veces al mismo
        verbose_name       = 'Seguimiento'                                 # Nombre singular en el admin
        verbose_name_plural = 'Seguimientos'                               # Nombre plural en el admin

    def __str__(self):
        return f'{self.seguidor} sigue a {self.seguido}'                   # Representación legible en el admin/shell


class SolicitudSeguimiento(models.Model):                                  # Modelo para gestionar solicitudes de seguimiento
    DE_PENDIENTE = 'pendiente'                                             # Constante: solicitud enviada, sin respuesta
    DE_ACEPTADA  = 'aceptada'                                              # Constante: solicitud aceptada

    ESTADOS = [
        (DE_PENDIENTE, 'Pendiente'),                                       # Opción pendiente para el campo choices
        (DE_ACEPTADA,  'Aceptada'),                                        # Opción aceptada para el campo choices
    ]

    solicitante  = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name='solicitudes_enviadas')  # Usuario que envía la solicitud
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name='solicitudes_recibidas') # Usuario que recibe la solicitud
    estado       = models.CharField(max_length=10, choices=ESTADOS, default=DE_PENDIENTE) # Estado actual de la solicitud
    fecha        = models.DateTimeField(auto_now_add=True)                 # Fecha en que se envió la solicitud

    class Meta:
        unique_together     = ('solicitante', 'destinatario')              # Evita solicitudes duplicadas entre los mismos usuarios
        verbose_name        = 'Solicitud de seguimiento'                   # Nombre singular en el admin
        verbose_name_plural = 'Solicitudes de seguimiento'                 # Nombre plural en el admin

    def __str__(self):
        return f'{self.solicitante} → {self.destinatario} ({self.estado})' # Representación legible en el admin/shell