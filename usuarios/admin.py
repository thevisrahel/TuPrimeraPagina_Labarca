from django.contrib import admin                                           # Módulo de administración de Django
from .models import InfoExtra                                              # Importa el modelo InfoExtra del módulo actual

admin.site.register(InfoExtra)                                             # Registra InfoExtra para gestionarlo desde el panel admin