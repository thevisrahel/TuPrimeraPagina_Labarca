from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_viaje, name='crear_viaje'),
    path('listar/', views.listar_viajes, name='listar_viajes'),
    path('viajes/<int:id_viaje>/', views.detalle_viajes, name='detalle_viaje')
    
]