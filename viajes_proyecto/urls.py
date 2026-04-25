"""
URL configuration for viajes_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin                                                            # Importa el módulo admin de Django para gestionar el panel de administración
from django.urls import path, include                                                       # 'path' define rutas URL, 'include' permite referenciar URLs de otras apps
from django.conf import settings                                                            # Importa la configuración global del proyecto (settings.py)
from django.conf.urls.static import static                                                  # Permite servir archivos estáticos/media durante el desarrollo

urlpatterns = [                                                                             # Lista principal de URLs del proyecto
    path('admin/', admin.site.urls),                                                        # Panel de administración de Django → http://localhost:8000/admin/

    path('', include('viajes_app.urls')),                                                   # Rutas raíz → delega al archivo urls.py de la app 'viajes_app'
    path('fotos/', include('fotos_app.urls')),                                              # Rutas de fotos → delega al urls.py de 'fotos_app'
    path('usuarios/', include('usuarios.urls')),                                            # Rutas de usuarios → delega al urls.py de 'usuarios'    
    path('comentarios/', include('comentarios.urls')),                                      # Rutas de comentarios → delega al urls.py de 'comentarios'
    path('social/', include('social.urls')),
]

if settings.DEBUG:                                                                          # Solo en modo desarrollo (DEBUG=True), Django sirve los archivos subidos por usuarios (imágenes, documentos, etc.). En producción esto lo maneja el servidor web
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            # MEDIA_URL: la URL pública  →  ej: /media/. MEDIA_ROOT: la carpeta física donde están guardados los archivos