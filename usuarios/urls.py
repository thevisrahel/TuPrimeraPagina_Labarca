from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrrar-sesion/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='cerrar_sesion'),  
    path('registro/', views.registrarse, name='registro'),    
    path('perfil/', views.perfil, name='perfil'), 
    
]