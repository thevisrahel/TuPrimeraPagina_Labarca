from django.urls import path
from . import views                                                                                         # Importa las vistas de esta misma app (el punto = carpeta actual)

app_name = 'viajes_app'                                                                                     # Nombre del espacio de URLs, permite referenciarlas como 'viajes_app:inicio', 'viajes_app:crear_viaje', etc. Evita conflictos si dos apps tienen rutas con el mismo nombre

urlpatterns = [
    path('', views.inicio, name='inicio'),                                                                  # http://localhost:8000/
    path('crear/', views.crear_viaje, name='crear_viaje'),                                                  # http://localhost:8000/crear/
    path('listar/', views.listar_viajes, name='listar_viajes'),                                             # http://localhost:8000/listar/
    path('viajes/<int:id_viaje>/', views.detalle_viajes, name='detalle_viaje'),                             # http://localhost:8000/viajes/5/
    path('viajes/<int:id_viaje>/actualizar/', views.actualizar_viajes, name='actualizar_viaje'),            # http://localhost:8000/viajes/5/actualizar/
    path('viajes/<int:id_viaje>/eliminar/', views.eliminar_viajes, name='eliminar_viaje'),                  # http://localhost:8000/viajes/5/eliminar/
    path('viaje/<int:viaje_id>/like/', views.toggle_like, name='toggle_like'),                              # http://localhost:8000/viaje/5/like/
        
    
]