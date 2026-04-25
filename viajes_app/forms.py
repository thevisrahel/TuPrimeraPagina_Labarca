from django import forms                                                                          # Importa el módulo de formularios de Django
from .models import Viaje                                                                         # Importa el modelo Viaje para crear el formulario basado en él


class ViajeForm(forms.ModelForm):                                                                 # ModelForm = formulario que se genera automáticamente a partir de un modelo

    class Meta:                                                                                   # Configuración interna del formulario
        model = Viaje                                                                             # Indica qué modelo se va a usar
        fields = [                                                                                # Campos que aparecerán en el formulario
            'region',
            'pais',
            'sitio_turistico',
            'descripcion',
            'fecha',
            'imagen'
        ]

        widgets = {                                                                               # Widgets = personalización visual de los campos (HTML)
            'fecha': forms.DateInput(
                format='%Y-%m-%d',        
                attrs={
                    'type': 'date',
                    'class': 'form-control'
            }),

            'region': forms.TextInput(attrs={                                                     # Clase de Bootstrap para estilos bonitos
                'class': 'form-control'
            }),

            'pais': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'sitio_turistico': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'descripcion': forms.Textarea(attrs={                                                 # Área de texto más grande (4 filas)
                'class': 'form-control',
                'rows': 4
            }),

            'imagen': forms.ClearableFileInput(attrs={                                            # Input para subir archivos (imagen)
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):                                                          # Constructor del formulario (se ejecuta al crear el form)
        super().__init__(*args, **kwargs) 
        
        self.fields['fecha'].input_formats = ['%Y-%m-%d']#                                        # Llama al constructor original de Django

        if 'imagen' in self.fields:                                                               # Verifica que el campo imagen exista
            self.fields['imagen'].widget.clear_checkbox_label = ''                                # Quita el texto "Clear" (checkbox para eliminar imagen)
            self.fields['imagen'].widget.initial_text = ''                                        # Quita el texto tipo "Currently: imagen.jpg"