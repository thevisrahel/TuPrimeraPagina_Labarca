from django.contrib import admin            # Importa el panel de administración de Django
from .models import Foto                   # Importa el modelo Foto


admin.site.register(Foto)                  # Registra el modelo Foto para que aparezca en el admin