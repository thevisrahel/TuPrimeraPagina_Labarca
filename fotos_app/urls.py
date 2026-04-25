from django.urls import path                               # Función para definir rutas URL en Django
from .views import SubirFotoView, EliminarFotoView         # Importa vistas específicas
app_name = 'fotos'                                         # Namespace para evitar conflictos de nombres


urlpatterns = [
    path('subir/<int:viaje_id>/', SubirFotoView.as_view(), name='subir'),           # Ruta para subir fotos a un viaje
    path('eliminar/<int:id_foto>/', EliminarFotoView.as_view(), name='eliminar_foto'),  # Ruta para eliminar una foto
]