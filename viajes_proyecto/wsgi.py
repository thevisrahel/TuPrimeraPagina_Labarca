"""
WSGI config for viajes_proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viajes_proyecto.settings')             # Le dice a Django qué archivo settings.py usar

application = get_wsgi_application()                                                    # Crea la aplicación WSGI lista para que el servidor web la use.
