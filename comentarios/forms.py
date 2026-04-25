from django import forms                               # Importa el sistema de formularios de Django
from .models import Comentario                         # Importa el modelo Comentario


class ComentarioForm(forms.ModelForm):                 # Formulario basado en el modelo Comentario

    class Meta:
        model = Comentario                             # Modelo asociado al formulario

        fields = ['texto']                             # Solo incluye el campo 'texto'

        widgets = {
            'texto': forms.Textarea(                   # Usa un textarea en lugar de input simple
                attrs={
                    'placeholder': 'Escribe un comentario...',  # Texto de ayuda dentro del campo
                    'rows': 2                         # Altura inicial del textarea
                }
            )
        }