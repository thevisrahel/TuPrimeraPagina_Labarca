from django import forms
from .models import Viaje

class ViajeForm(forms.ModelForm):
    
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Viaje
        fields = ['destino', 'descripcion', 'fecha', 'imagen']
        widgets = {
            'fecha' : forms.DateInput(attrs={'type':'date'})
        }