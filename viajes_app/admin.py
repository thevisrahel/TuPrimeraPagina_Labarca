from django.contrib import admin                                                                  # Importa el módulo de administración de Django
from .models import Viaje                                                                         # Importa el modelo Viaje para registrarlo en el admin


class ViajeAdmin(admin.ModelAdmin):                                                               # Personaliza cómo se ve el modelo Viaje en el panel admin
    list_display = ['id', 'propietario', 'region', 'sitio_turistico', 'fecha', 'creado']          # Columnas que se muestran en la lista de viajes
    list_filter = ['region', 'fecha']                                                             # Filtros laterales para filtrar por región o fecha
    search_fields = ['region', 'sitio_turistico']                                                 # Campos por los que se puede buscar en la barra de búsqueda


admin.site.register(Viaje, ViajeAdmin)                                                            # Registra el modelo Viaje con su configuración personalizada en el admin