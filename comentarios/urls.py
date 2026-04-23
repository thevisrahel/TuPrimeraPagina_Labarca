from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('agregar/<int:viaje_id>/', views.agregar_comentario, name='agregar'),
    path('eliminar/<int:comentario_id>/', views.eliminar_comentario, name='eliminar'),
]