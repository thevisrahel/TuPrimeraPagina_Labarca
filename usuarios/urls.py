from django.urls import path                                               # Función para definir rutas URL
from . import views                                                        # Importa las vistas del módulo actual
from django.contrib.auth import views as auth_views                        # Vistas de autenticación integradas de Django
from .views import CambioDePass                                            # Vista de cambio de contraseña personalizada

app_name = 'usuarios'                                                      # Namespace de la app para usar en reverse/redirect

urlpatterns = [

    # ---------------- AUTENTICACIÓN ----------------
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),  # Login del usuario
    path(
        'cerrar-sesion/',                                                  # URL para cerrar sesión
        auth_views.LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'),  # Vista de logout con template propio
        name='cerrar_sesion'                                               # Nombre de la ruta
    ),
    path('registro/', views.registrarse, name='registro'),                 # Registro de nuevo usuario


    # ---------------- RECUPERACIÓN DE CONTRASEÑA ----------------
    path(
        'password-reset/',                                                 # URL para solicitar reseteo de contraseña
        auth_views.PasswordResetView.as_view(
            template_name='usuarios/password_reset_form.html',            # Template del formulario de reset
            email_template_name='usuarios/password_reset_email.html',     # Template del email que se envía al usuario
            success_url='/usuarios/password-reset/done/'                  # Redirige aquí tras enviar el email
        ),
        name='password_reset'                                             # Nombre de la ruta
    ),
    path(
        'password-reset/done/',                                            # URL de confirmación de email enviado
        auth_views.PasswordResetDoneView.as_view(
            template_name='usuarios/password_reset_done.html'             # Template de pantalla de éxito
        ),
        name='password_reset_done'                                        # Nombre de la ruta
    ),
    path(
        'reset/<uidb64>/<token>/',                                         # URL con token único para confirmar el reset
        auth_views.PasswordResetConfirmView.as_view(
            template_name='usuarios/password_reset_confirm.html',         # Template del formulario de nueva contraseña
            success_url='/usuarios/reset/done/'                           # Redirige aquí tras cambiar la contraseña
        ),
        name='password_reset_confirm'                                     # Nombre de la ruta
    ),
    path(
        'reset/done/',                                                     # URL final: reset completado con éxito
        auth_views.PasswordResetCompleteView.as_view(
            template_name='usuarios/password_reset_complete.html'         # Template de confirmación final
        ),
        name='password_reset_complete'                                    # Nombre de la ruta
    ),


    # ---------------- PERFIL ----------------
    path('perfil/', views.perfil, name='perfil'),                          # Ver perfil propio
    path('perfil/actualizar/', views.actualizar_perfil, name='actualizar_perfil'),          # Editar datos del perfil
    path('perfil/actualizar/password/', CambioDePass.as_view(), name='actualizar_password'), # Cambiar contraseña
    path('perfil/eliminar-avatar/', views.eliminar_avatar, name='eliminar_avatar'),         # Eliminar avatar personalizado
    path('privacidad/', views.toggle_privacidad, name='toggle_privacidad'),                 # Alternar perfil público/privado
    path('eliminar-perfil/', views.eliminar_perfil, name='eliminar_perfil'),                # Eliminar cuenta del usuario


    # ---------------- GENERAL ----------------
    path('about-me/', views.about_me, name='about_me'),                   # Página informativa sobre el sitio
]