from django.contrib import admin                                           # Módulo de administración de Django
from .models import Seguimiento, SolicitudSeguimiento                      # Importa los modelos de la app social

admin.site.register(Seguimiento)                                           # Registra Seguimiento en el panel admin
admin.site.register(SolicitudSeguimiento)                                  # Registra SolicitudSeguimiento en el panel admin