from django import forms
from .models import Proyecto, Commentario, Persona

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'overview', 'descripcion', 'documentacion', 'categoria', 'destacado']
        widgets = {
            'overview': forms.Textarea(attrs={'class': 'overview-field'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentario
        fields = ['comentari'] 
        widgets = {
            'comentari': forms.Textarea(attrs={'class': 'comentari-field'}),
        }       
        

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['imagen', 'dni', 'fecha_nacimiento', 'telefono']