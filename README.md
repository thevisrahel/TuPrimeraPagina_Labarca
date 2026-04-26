# 🌍 Viajes App

Plataforma web de viajes y experiencias sociales desarrollada con Django. Permite a los usuarios registrar viajes, subir fotos, interactuar con otros usuarios y gestionar su red de seguidores.

---

## 🚀 Tecnologías

- Python 3.14
- Django 6.0
- SQLite
- Bootstrap 5
- Font Awesome 6

---

## 📁 Estructura del proyecto

```
viajes_proyecto/
│
├── viajes_app/        # Gestión de viajes y likes
├── fotos_app/         # Subida y eliminación de fotos
├── usuarios/          # Autenticación y perfil propio
├── social/            # Relaciones entre usuarios
├── comentarios/       # Comentarios y respuestas
└── templates/         # Templates globales (base.html)
```

---

## ⚙️ Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd viajes_proyecto

# 2. Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate        # Windows
source .venv/bin/activate            # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Correr el servidor
python manage.py runserver
```

---

## 🧩 Apps

### `usuarios`
Maneja todo lo relacionado con el usuario propio.

| Vista | URL | Descripción |
|---|---|---|
| Login | `/usuarios/iniciar-sesion/` | Inicio de sesión |
| Registro | `/usuarios/registro/` | Crear cuenta |
| Perfil | `/usuarios/perfil/` | Ver perfil propio |
| Actualizar perfil | `/usuarios/perfil/actualizar/` | Editar datos |
| Cambiar password | `/usuarios/perfil/actualizar/password/` | Cambiar contraseña |
| Eliminar avatar | `/usuarios/perfil/eliminar-avatar/` | Borrar foto de perfil |
| Privacidad | `/usuarios/privacidad/` | Alternar perfil público/privado |
| Eliminar cuenta | `/usuarios/eliminar-perfil/` | Borrar cuenta permanentemente |
| About me | `/usuarios/about-me/` | Página del desarrollador |

### `social`
Maneja las relaciones e interacciones entre usuarios.

| Vista | URL | Descripción |
|---|---|---|
| Buscar | `/social/buscar/` | Buscar usuarios |
| Ver perfil | `/social/<username>/` | Ver perfil público de otro usuario |
| Seguir | `/social/<username>/seguir/` | Enviar solicitud de seguimiento |
| Dejar de seguir | `/social/<username>/dejar-de-seguir/` | Dejar de seguir |
| Solicitudes | `/social/solicitudes/` | Ver solicitudes pendientes |
| Aceptar solicitud | `/social/solicitudes/<id>/aceptar/` | Aceptar solicitud |
| Rechazar solicitud | `/social/solicitudes/<id>/rechazar/` | Rechazar solicitud |
| Seguidores | `/social/<username>/seguidores/` | Lista de seguidores |
| Siguiendo | `/social/<username>/siguiendo/` | Lista de seguidos |
| Viaje público | `/social/<username>/viaje/<id>/` | Ver viaje de otro usuario |

### `viajes_app`
Gestión de viajes y likes.

| Vista | URL | Descripción |
|---|---|---|
| Inicio | `/viajes/` | Página de inicio |
| Crear viaje | `/viajes/crear/` | Crear nuevo viaje |
| Lista de viajes | `/viajes/lista/` | Ver todos los viajes propios |
| Detalle viaje | `/viajes/<id>/` | Ver detalle de un viaje |
| Like | `/viaje/<id>/like/` | Dar/quitar like |

### `fotos_app`
Subida y eliminación de fotos por viaje.

### `comentarios`
Comentarios y respuestas anidadas en viajes.

---

## 🔐 Modelos principales

### `usuarios.InfoExtra`
Extiende el modelo `User` con avatar, fecha de nacimiento y privacidad.

### `social.Seguimiento`
Relación de seguimiento entre dos usuarios.

### `social.SolicitudSeguimiento`
Solicitud de seguimiento para perfiles privados. Estados: `pendiente`, `aceptada`, `rechazada`.

### `viajes_app.Viaje`
Viaje con región, país, sitio turístico, descripción, fecha e imagen de cabecera.

### `viajes_app.Like`
Like de un usuario a un viaje. Único por par usuario-viaje.

---

## 🔒 Privacidad

Los perfiles pueden ser **públicos** o **privados**. En perfiles privados:
- Los viajes solo son visibles para seguidores aprobados
- Seguir requiere enviar una solicitud que el usuario debe aceptar
- Las listas de seguidores/siguiendo también están restringidas

---

## 📧 Recuperación de contraseña

Configurado con SMTP de Gmail. Requiere las siguientes variables en `settings.py`:

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_app_password'
```

---

## 👤 Autor

**Elvis Labarca**

- [LinkedIn](https://www.linkedin.com/in/elvislabarca/)
- [GitHub](https://github.com/thevisrahel)
