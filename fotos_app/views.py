from django.views import View                                         # Clase base para vistas basadas en clases
from django.shortcuts import render, redirect, get_object_or_404      # Funciones útiles de Django
from viajes_app.models import Viaje                                   # Modelo de viajes
from .models import Foto                                              # Modelo de fotos
from django.contrib.auth.mixins import LoginRequiredMixin             # Requiere que el usuario esté logueado


class SubirFotoView(LoginRequiredMixin, View):                        # Vista para subir fotos

    def get(self, request, viaje_id):
        viaje = get_object_or_404(Viaje, id=viaje_id)                 # Obtiene el viaje o lanza 404

        return render(request, 'fotos_app/subir.html', {              # Renderiza el template
            'viaje': viaje                                            # Envía el viaje al template
        })

    def post(self, request, viaje_id):
        viaje = get_object_or_404(Viaje, id=viaje_id)                 # Vuelve a obtener el viaje (seguridad)

        files = request.FILES.getlist('imagen')                       # Obtiene lista de imágenes subidas

        for f in files:                                               # Itera sobre cada archivo recibido
            Foto.objects.create(
                viaje=viaje,                                          # Asocia la foto al viaje
                imagen=f                                              # Guarda el archivo de imagen
            )

        return redirect('viajes_app:detalle_viaje', id_viaje=viaje.id)   # Redirige al detalle del viaje


class EliminarFotoView(LoginRequiredMixin, View):                     # Vista para eliminar fotos

    def post(self, request, id_foto):
        foto = get_object_or_404(Foto, id=id_foto)                    # Obtiene la foto o lanza 404

        viaje = foto.viaje                                            # Guarda el viaje antes de eliminar la foto

        if foto.imagen:                                               # Verifica si existe archivo físico
            foto.imagen.delete(save=False)                            # Elimina el archivo del sistema sin guardar aún

        foto.delete()                                                 # Elimina el registro de la base de datos

        return redirect('viajes_app:detalle_viaje', id_viaje=viaje.id)   # Redirige al detalle del viaje