from django.shortcuts import render, redirect, get_object_or_404          # Funciones para renderizar, redirigir y obtener objetos
from django.contrib.auth.decorators import login_required                  # Decorador que exige autenticación
from django.contrib.auth.models import User                                # Modelo de usuario integrado de Django
from django.db.models import Q                                             # Permite hacer consultas con OR en los filtros

from social.models import Seguimiento, SolicitudSeguimiento                # Modelos de relaciones sociales
from usuarios.models import InfoExtra                                      # Modelo de información extra del usuario
from viajes_app.models import Viaje                                        # Modelo de viajes


def buscar_usuarios(request):                                              # Vista para buscar usuarios por nombre o username

    query = request.GET.get('q')                                           # Obtiene el texto de búsqueda del parámetro GET 'q'
    resultados = User.objects.none()                                       # Queryset vacío por defecto

    if query:                                                              # Solo busca si hay texto ingresado
        resultados = User.objects.filter(
            Q(username__icontains=query) |                                 # Busca por username
            Q(first_name__icontains=query) |                              # O por nombre
            Q(last_name__icontains=query)                                  # O por apellido
        )

        if request.user.is_authenticated:                                  # Si el usuario está logueado
            resultados = resultados.exclude(id=request.user.id)           # Excluye al propio usuario de los resultados

    return render(request, 'social/buscar_usuarios.html', {               # Renderiza el template con los resultados
        'resultados': resultados,                                          # Lista de usuarios encontrados
        'query': query                                                     # Texto buscado para mostrarlo en el input
    })

def ver_perfil(request, username):                                         # Vista para ver el perfil público de un usuario

    usuario = get_object_or_404(User, username=username)                  # Obtiene el usuario o devuelve 404
    InfoExtra.objects.get_or_create(user=usuario)                         # Crea InfoExtra si no existe para evitar errores

    es_privado = usuario.info.es_privado                                  # Verifica si el perfil es privado

    es_seguidor = False                                                    # Por defecto no es seguidor
    viajes = []                                                            # Por defecto no muestra viajes

    if request.user.is_authenticated:                                      # Si el visitante está logueado
        es_seguidor = Seguimiento.objects.filter(
            seguidor=request.user,                                         # El visitante sigue
            seguido=usuario                                                # al dueño del perfil
        ).exists()

    if not es_privado or es_seguidor or request.user == usuario:          # Si puede ver el contenido
        viajes = usuario.viajes.order_by('-fecha')                        # Trae los viajes ordenados por fecha descendente

    seguidores = usuario.seguidores.count()                               # Cantidad de seguidores del usuario
    siguiendo = usuario.siguiendo.count()                                  # Cantidad de usuarios que sigue

    solicitud_pendiente = False                                            # Por defecto no hay solicitud pendiente
    if request.user.is_authenticated:                                      # Si el visitante está logueado
        solicitud_pendiente = SolicitudSeguimiento.objects.filter(
            solicitante=request.user,                                      # El visitante envió la solicitud
            destinatario=usuario,                                          # Al dueño del perfil
            estado='pendiente'                                             # Y está pendiente de aceptación
        ).exists()

    return render(request, 'social/ver_perfil.html', {                    # Renderiza el template del perfil
        'usuario': usuario,                                                # Usuario del perfil visitado
        'viajes': viajes,                                                  # Viajes visibles según privacidad
        'es_seguidor': es_seguidor,                                        # Si el visitante sigue al usuario
        'es_privado': es_privado,                                          # Si el perfil es privado
        'seguidores': seguidores,                                          # Cantidad de seguidores
        'siguiendo': siguiendo,                                            # Cantidad de seguidos
        'solicitud_pendiente': solicitud_pendiente,                        # Si hay solicitud enviada pendiente
    })

@login_required                                                            # Requiere autenticación
def seguir(request, username):                                             # Vista para enviar solicitud de seguimiento

    usuario_a_seguir = get_object_or_404(User, username=username)         # Obtiene el usuario a seguir

    if request.user != usuario_a_seguir:                                   # Evita que el usuario se siga a sí mismo
        SolicitudSeguimiento.objects.get_or_create(
            solicitante=request.user,                                      # El que envía la solicitud
            destinatario=usuario_a_seguir                                  # El que la recibe
        )

    return redirect('social:ver_perfil', username=username)                # Vuelve al perfil del usuario

@login_required                                                            # Requiere autenticación
def dejar_de_seguir(request, username):                                    # Vista para dejar de seguir a un usuario

    usuario_a_dejar = get_object_or_404(User, username=username)          # Obtiene el usuario a dejar de seguir

    Seguimiento.objects.filter(
        seguidor=request.user,                                             # El usuario actual
        seguido=usuario_a_dejar                                            # Deja de seguir a este usuario
    ).delete()                                                             # Elimina la relación de seguimiento

    SolicitudSeguimiento.objects.filter(
        solicitante=request.user,                                          # También elimina la solicitud asociada
        destinatario=usuario_a_dejar
    ).delete()                                                             # Borra la solicitud

    return redirect('social:ver_perfil', username=username)                # Vuelve al perfil del usuario

@login_required                                                            # Requiere autenticación
def solicitudes(request):                                                  # Vista de solicitudes y notificaciones

    solicitudes_pendientes = request.user.solicitudes_recibidas.filter(   # Solicitudes de seguimiento pendientes
        estado='pendiente'
    )

    from comentarios.models import Notificacion                            # Importa el modelo de notificaciones

    notificaciones = request.user.notificaciones.all().order_by('-creada') # Trae todas ordenadas por fecha descendente

    request.user.notificaciones.filter(leida=False).update(leida=True)    # Marca todas las no leídas como leídas al entrar

    return render(request, 'social/solicitudes.html', {                   # Renderiza el template
        'solicitudes': solicitudes_pendientes,                             # Solicitudes de seguimiento pendientes
        'notificaciones': notificaciones,                                  # Todas las notificaciones del usuario
    })

@login_required                                                            # Requiere autenticación
def aceptar_solicitud(request, solicitud_id):                             # Vista para aceptar una solicitud de seguimiento

    solicitud = get_object_or_404(
        SolicitudSeguimiento,
        id=solicitud_id,
        destinatario=request.user                                          # Solo puede aceptar el destinatario
    )

    solicitud.estado = 'aceptada'                                          # Cambia el estado a aceptada
    solicitud.save()                                                       # Guarda el cambio en la BD

    Seguimiento.objects.get_or_create(
        seguidor=solicitud.solicitante,                                    # Crea la relación de seguimiento
        seguido=request.user                                               # El destinatario es ahora seguido
    )

    return redirect('social:solicitudes')                                  # Vuelve a la página de notificaciones

@login_required                                                            # Requiere autenticación
def rechazar_solicitud(request, solicitud_id):                            # Vista para rechazar una solicitud de seguimiento

    solicitud = get_object_or_404(
        SolicitudSeguimiento,
        id=solicitud_id,
        destinatario=request.user                                          # Solo puede rechazar el destinatario
    )

    solicitud.delete()                                                     # Elimina la solicitud directamente

    return redirect('social:solicitudes')                                  # Vuelve a la página de notificaciones

def detalle_viaje_publico(request, username, id_viaje):                   # Vista para ver el detalle de un viaje público

    usuario = get_object_or_404(User, username=username)                  # Obtiene el dueño del viaje
    viaje = get_object_or_404(Viaje, id=id_viaje, propietario=usuario)   # Obtiene el viaje o devuelve 404

    es_privado = usuario.info.es_privado                                  # Verifica si el perfil es privado

    es_seguidor = False                                                    # Por defecto no es seguidor
    if request.user.is_authenticated:                                      # Si el visitante está logueado
        es_seguidor = Seguimiento.objects.filter(
            seguidor=request.user,                                         # El visitante sigue
            seguido=usuario                                                # al dueño del viaje
        ).exists()

    if es_privado and not es_seguidor and request.user != usuario:        # Si no tiene permiso para ver el viaje
        return redirect('social:ver_perfil', username=username)           # Redirige al perfil público

    usuario_dio_like = False                                               # Por defecto no dio like
    if request.user.is_authenticated:                                      # Si el visitante está logueado
        usuario_dio_like = viaje.likes.filter(user=request.user).exists() # Verifica si ya dio like

    return render(request, 'social/detalle_viaje_publico.html', {         # Renderiza el template del viaje
        'usuario': usuario,                                                # Dueño del viaje
        'viaje': viaje,                                                    # Objeto viaje
        'usuario_dio_like': usuario_dio_like,                              # Si el visitante ya dio like
    })

def lista_seguidores(request, username):                                   # Vista para listar seguidores de un usuario

    usuario = get_object_or_404(User, username=username)                  # Obtiene el usuario
    es_privado = usuario.info.es_privado                                  # Verifica privacidad

    es_seguidor = False                                                    # Por defecto no es seguidor
    if request.user.is_authenticated:                                      # Si el visitante está logueado
        es_seguidor = Seguimiento.objects.filter(
            seguidor=request.user,
            seguido=usuario
        ).exists()

    if es_privado and not es_seguidor and request.user != usuario:        # Si no tiene permiso
        return redirect('social:ver_perfil', username=username)           # Redirige al perfil

    seguidores = User.objects.filter(siguiendo__seguido=usuario)          # Obtiene todos los seguidores del usuario

    return render(request, 'social/lista_seguidores.html', {              # Renderiza el template
        'usuario': usuario,                                                # Usuario dueño de la lista
        'usuarios': seguidores,                                            # Lista de seguidores
        'titulo': f'Seguidores de {usuario.username}'                     # Título dinámico de la página
    })

def lista_siguiendo(request, username):                                    # Vista para listar usuarios que sigue alguien

    usuario = get_object_or_404(User, username=username)                  # Obtiene el usuario
    es_privado = usuario.info.es_privado                                  # Verifica privacidad

    es_seguidor = False                                                    # Por defecto no es seguidor
    if request.user.is_authenticated:                                      # Si el visitante está logueado
        es_seguidor = Seguimiento.objects.filter(
            seguidor=request.user,
            seguido=usuario
        ).exists()

    if es_privado and not es_seguidor and request.user != usuario:        # Si no tiene permiso
        return redirect('social:ver_perfil', username=username)           # Redirige al perfil

    siguiendo = User.objects.filter(seguidores__seguidor=usuario)         # Obtiene todos los usuarios que sigue

    return render(request, 'social/lista_seguidores.html', {              # Reutiliza el mismo template de seguidores
        'usuario': usuario,                                                # Usuario dueño de la lista
        'usuarios': siguiendo,                                             # Lista de usuarios seguidos
        'titulo': f'{usuario.username} sigue a'                           # Título dinámico de la página
    })

@login_required                                                            # Requiere autenticación
def eliminar_seguidor(request, username):                                  # Vista para eliminar un seguidor propio

    seguidor = get_object_or_404(User, username=username)                  # Obtiene al usuario que nos sigue

    Seguimiento.objects.filter(
        seguidor=seguidor,                                                 # El que nos sigue
        seguido=request.user                                               # Nosotros como seguidos
    ).delete()                                                             # Elimina la relación de seguimiento

    SolicitudSeguimiento.objects.filter(
        solicitante=seguidor,                                              # El que nos seguía
        destinatario=request.user                                          # Nosotros
    ).delete()                                                             # Borra la solicitud asociada

    return redirect('social:lista_seguidores', username=request.user.username) # Vuelve a nuestra lista de seguidores

@login_required                                                            # Requiere autenticación
def eliminar_notificacion(request, notificacion_id):                      # Vista para eliminar una notificación propia

    from comentarios.models import Notificacion                            # Importa el modelo de notificaciones

    notificacion = get_object_or_404(
        Notificacion,
        id=notificacion_id,
        destinatario=request.user                                          # Solo puede borrar sus propias notificaciones
    )
    notificacion.delete()                                                  # Elimina la notificación de la BD

    return redirect('social:solicitudes')                                  # Vuelve a la página de notificaciones