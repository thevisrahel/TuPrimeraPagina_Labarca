from django import forms                                  # Importa el módulo de formularios de Django
from .models import Foto                                  # Importa el modelo Foto


class FotoForm(forms.ModelForm):                          # Formulario basado en el modelo Foto

    imagen = forms.ImageField(                            # Campo para subir imágenes
        widget=forms.ClearableFileInput(                  # Widget que permite seleccionar archivos
            attrs={
                'multiple': True                          # Permite seleccionar múltiples imágenes
            }
        )
    )

    class Meta:
        model = Foto                                      # Modelo al que está ligado el formulario
        fields = ['imagen']                               # Campo que se incluirá en el formulario