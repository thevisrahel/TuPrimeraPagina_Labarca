# import os
# from django.shortcuts import render, redirect, get_object_or_404
# from viajes_app.models import Viaje
# from .models import Foto

# def subir_foto(request, viaje_id):
#     viaje = Viaje.objects.get(id=viaje_id)

#     if request.method == "POST":
#         files = request.FILES.getlist('imagen')

#         for f in files:
#             Foto.objects.create(
#                 viaje=viaje,
#                 imagen=f
#             )

#         return redirect('viajes_app:detalle_viaje', id_viaje=viaje.id)
    
#     return render(request, 'fotos_app/subir.html')

# def eliminar_foto(request, id_foto):
#     foto = get_object_or_404 (Foto, id=id_foto)
#     viaje = foto.viaje

#     if foto.imagen:
#         foto.imagen.delete(save=False)

#     foto.delete()

#     return redirect('viajes_app:detalle_viaje', viaje.id)

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from viajes_app.models import Viaje
from .models import Foto


class SubirFotoView(View):

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


class EliminarFotoView(View):

    def post(self, request, id_foto):
        foto = get_object_or_404(Foto, id=id_foto)
        viaje = foto.viaje

        if foto.imagen:
            foto.imagen.delete(save=False)

        foto.delete()

        return redirect('viajes_app:detalle_viaje', id_viaje=viaje.id)