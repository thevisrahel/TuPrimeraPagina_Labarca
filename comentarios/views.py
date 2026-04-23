from django.shortcuts import redirect, get_object_or_404
from viajes_app.models import Viaje
from .models import Comentario
from .forms import ComentarioForm
from django.contrib import messages


def agregar_comentario(request, viaje_id):
    if not request.user.is_authenticated:
        return redirect('usuarios:iniciar_sesion')

    viaje = get_object_or_404(Viaje, id=viaje_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        padre_id = request.POST.get('padre_id')

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.viaje = viaje
            comentario.padre_id = padre_id if padre_id else None
            comentario.save()

    return redirect(request.META.get('HTTP_REFERER', 'viajes:inicio'))


def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    viaje = comentario.viaje
    username = viaje.propietario.username
    viaje_id = viaje.id

    if request.user == comentario.usuario or request.user == viaje.propietario:
        comentario.delete()
        messages.success(request, "Comentario eliminado")
    else:
        messages.error(request, "No tienes permiso")

    # Redirige de vuelta a donde vino
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)

    return redirect('usuarios:detalle_viaje_publico', username=username, id_viaje=viaje_id)