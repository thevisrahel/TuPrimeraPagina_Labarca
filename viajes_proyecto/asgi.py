"""
ASGI config for viajes_proyecto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application                                       # versión async (vs wsgi que es síncrono)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viajes_proyecto.settings')             # Apunta al settings.py del proyecto

application = get_asgi_application()                                                    # Crea la aplicación ASGI lista para servidores
