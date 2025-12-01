from django import forms
from .models import Proyecto, Habilidad


class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'experiencia']


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'titulo',
            'descripcion',
            'imagen',
            'demo_url',
            'repo_url',
            'habilidades'
        ]
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
        