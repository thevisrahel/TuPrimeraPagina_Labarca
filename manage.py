#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys                                                                                  # Captura los comandos que escritos en la terminal


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viajes_proyecto.settings')             # Le dice a Django qué settings.py usar
    try:
        from django.core.management import execute_from_command_line                        # Importa la función que ejecuta los comandos de Django
    except ImportError as exc:                                                              # Si Django no está instalado o el entorno virtual no está activado, muestra un mensaje claro explicando qué salió mal
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)                                                     # Ejecuta el comando que escribiste en la terminal


if __name__ == '__main__':                                                                  #Solo ejecuta main() si corres este archivo directamente (no cuando otro archivo lo importa)
    main()
