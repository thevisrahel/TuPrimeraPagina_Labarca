from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from viajes_app.models import Viaje
from .models import Foto
from django.contrib.auth.mixins import LoginRequiredMixin


class SubirFotoView(LoginRequiredMixin, View):

    def get(self, request, viaje_id):
        viaje = get_object_or_404(Viaje, id=viaje_id)
        return render(request, 'fotos_app/subir.html', {
            'viaje': viaje
        })

    def post(self, request, viaje_id):
        viaje = get_object_or_404(Viaje, id=viaje_id)
        files = request.FILES.getlist('imagen')

        for f in files:
            Foto.objects.create(
                viaje=viaje,
                imagen=f
            )

        return redirect('viajes_app:detalle_viaje', id_viaje=viaje.id)


class EliminarFotoView(LoginRequiredMixin, View):

    def post(self, request, id_foto):
        foto = get_object_or_404(Foto, id=id_foto)
        viaje = foto.viaje

        if foto.imagen:
            foto.imagen.delete(save=False)

        foto.delete()

        return redirect('viajes_app:detalle_viaje', id_viaje=viaje.id)