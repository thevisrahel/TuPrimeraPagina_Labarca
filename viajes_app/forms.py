from django import forms
from .models import Viaje

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['destino', 'descripcion', 'fecha']