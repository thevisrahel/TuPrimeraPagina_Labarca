from django.urls import path                                               # Función para definir rutas URL
from . import views                                                        # Importa las vistas del módulo actual

app_name = 'social'                                                        # Namespace de la app para usar en reverse/redirect

urlpatterns = [

    # ---------------- BUSCAR ----------------
    path('buscar/',                                                        # URL de búsqueda de usuarios
         views.buscar_usuarios,
         name='buscar_usuarios'),


    # ---------------- SOLICITUDES ----------------
    path('solicitudes/',                                                   # Página de solicitudes y notificaciones
         views.solicitudes,
         name='solicitudes'),

    path('solicitudes/<int:solicitud_id>/aceptar/',                       # Aceptar solicitud por su ID
         views.aceptar_solicitud,
         name='aceptar_solicitud'),

    path('solicitudes/<int:solicitud_id>/rechazar/',                      # Rechazar solicitud por su ID
         views.rechazar_solicitud,
         name='rechazar_solicitud'),

    path('eliminar-seguidor/<str:username>/',                             # Eliminar un seguidor propio
         views.eliminar_seguidor,
         name='eliminar_seguidor'),

    path('eliminar-notificacion/<int:notificacion_id>/',                  # Eliminar una notificación propia
         views.eliminar_notificacion,
         name='eliminar_notificacion'),


    # ---------------- PERFILES PÚBLICOS (siempre al final) ----------------
    path('<str:username>/seguir/',                                         # Enviar solicitud de seguimiento
         views.seguir,
         name='seguir'),

    path('<str:username>/dejar-de-seguir/',                               # Dejar de seguir a un usuario
         views.dejar_de_seguir,
         name='dejar_de_seguir'),

    path('<str:username>/seguidores/',                                     # Ver lista de seguidores
         views.lista_seguidores,
         name='lista_seguidores'),

    path('<str:username>/siguiendo/',                                      # Ver lista de seguidos
         views.lista_siguiendo,
         name='lista_siguiendo'),

    path('<str:username>/viaje/<int:id_viaje>/',                          # Ver detalle de un viaje público
         views.detalle_viaje_publico,
         name='detalle_viaje_publico'),

    path('<str:username>/',                                                # Ver perfil público — siempre el último
         views.ver_perfil,
         name='ver_perfil'),
]