Proyecto Django - Viajes

Funcionalidades

- Crear viajes por usuario
- Listar viajes (cada usuario ve los suyos)
- Ver detalle de cada viaje
- Actualizar y eliminar viajes
- Subir fotos a cada viaje
- Ver fotos asociadas a cada viaje
- Eliminar fotos de los viajes
- Búsqueda de viajes
- Sistema de autenticación (registro / inicio de sesión)

Sistema de usuarios

Cada cuenta de usuario:

- Puede crear sus propios viajes
- Solo puede ver y gestionar sus viajes
- No tiene acceso a los viajes de otros usuarios

Usuario administrador / staff

El proyecto incluye una cuenta de prueba con permisos de staff:

- Crear viajes
- Editar viajes
- Eliminar viajes
- Ver todos los viajes
- Gestionar fotos de cualquier viaje

Cuenta de prueba

Usuario: coderhouse_python
Contraseña: escribir la palabra comision y luego el número de la comisión

Funcionalidad de fotos

Cada viaje permite:

- Subir múltiples fotos
- Visualizar galería del viaje
- Eliminar fotos específicas

Instalación

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
