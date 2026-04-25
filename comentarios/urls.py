from django.urls import path                           # Función para definir rutas URL en Django
from . import views                                    # Importa todas las vistas del módulo actual

app_name = 'comentarios'                               # Namespace para evitar conflictos de nombres


urlpatterns = [
    path('agregar/<int:viaje_id>/', views.agregar_comentario, name='agregar'),       # Ruta para agregar un comentario a un viaje
    path('eliminar/<int:comentario_id>/', views.eliminar_comentario, name='eliminar'),  # Ruta para eliminar un comentario
]