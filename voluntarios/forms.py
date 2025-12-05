from django import forms
from .models import Evento, Voluntario

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email', 'telefono']

class AsignarVoluntariosForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['voluntarios']
        widgets = {
            'voluntarios': forms.CheckboxSelectMultiple
        }


class AsignarEventosForm(forms.Form): 
    eventos = forms.ModelMultipleChoiceField(
        queryset=Evento.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )