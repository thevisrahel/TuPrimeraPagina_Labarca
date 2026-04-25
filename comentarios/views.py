from django.shortcuts import redirect, get_object_or_404        # Funciones para redirigir y obtener objetos o 404
from viajes_app.models import Viaje                             # Modelo de viajes
from .models import Comentario, Notificacion                    # Modelos de comentarios y notificaciones
from .forms import ComentarioForm                              # Formulario de comentarios
from django.contrib import messages                            # Sistema de mensajes (éxito/error)


def agregar_comentario(request, viaje_id):                     # Vista para agregar un comentario
    if not request.user.is_authenticated:                      # Verifica si el usuario está autenticado
        return redirect('usuarios:iniciar_sesion')             # Redirige al login si no lo está

    viaje = get_object_or_404(Viaje, id=viaje_id)              # Obtiene el viaje o lanza 404

    if request.method == 'POST':                               # Solo procesa si es POST
        form = ComentarioForm(request.POST)                    # Instancia el formulario con datos enviados
        padre_id = request.POST.get('padre_id')                # Obtiene el ID del comentario padre (si es respuesta)

        if form.is_valid():                                    # Valida el formulario
            comentario = form.save(commit=False)               # Crea el objeto sin guardarlo aún
            comentario.usuario = request.user                  # Asigna el usuario actual
            comentario.viaje = viaje                           # Asigna el viaje
            comentario.padre_id = padre_id if padre_id else None   # Asigna comentario padre si existe
            comentario.save()                                  # Guarda el comentario en la BD

            if viaje.propietario != request.user:              # Evita notificarse a sí mismo
                Notificacion.objects.create(
                    destinatario=viaje.propietario,            # Usuario que recibe la notificación
                    remitente=request.user,                    # Usuario que hizo el comentario
                    tipo='comentario',                         # Tipo de notificación
                    comentario=comentario                      # Referencia al comentario creado
                )

            if padre_id:                                      # Si es respuesta a otro comentario
                padre = get_object_or_404(Comentario, id=padre_id)  # Obtiene el comentario padre

                if padre.usuario != request.user and padre.usuario != viaje.propietario:  # Evita duplicados
                    Notificacion.objects.create(
                        destinatario=padre.usuario,            # Notifica al autor del comentario padre
                        remitente=request.user,                # Usuario que responde
                        tipo='respuesta',                      # Tipo de notificación
                        comentario=comentario                  # Referencia al comentario creado
                    )

    return redirect(request.META.get('HTTP_REFERER', 'viajes:inicio'))  # Vuelve a la página anterior o inicio

def eliminar_comentario(request, comentario_id):              # Vista para eliminar un comentario
    comentario = get_object_or_404(Comentario, id=comentario_id)  # Obtiene el comentario o lanza 404

    viaje = comentario.viaje                                  # Obtiene el viaje asociado
    username = viaje.propietario.username                     # Username del propietario del viaje
    viaje_id = viaje.id                                       # ID del viaje

    if request.user == comentario.usuario or request.user == viaje.propietario:  # Verifica permisos
        comentario.delete()                                   # Elimina el comentario (y dependencias por CASCADE)
        messages.success(request, "Comentario eliminado")     # Mensaje de éxito
    else:
        messages.error(request, "No tienes permiso")           # Mensaje de error

    referer = request.META.get('HTTP_REFERER')                # Obtiene la URL anterior
    if referer:
        return redirect(referer)                              # Redirige a la página anterior

    return redirect('social:detalle_viaje_publico', username=username, id_viaje=viaje_id)  # Fallback si no hay referer