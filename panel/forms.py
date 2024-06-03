from django import forms
from .models import Proyecto, Commentario, Persona, T_Proyectos, GlobalSettings
from datetime import date

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
        
        
        
#proyectos de interaccion social 
class T_ProyectosForm(forms.ModelForm):
    class Meta:
        model = T_Proyectos
        fields = ['S_Titulo','Fecha_Inicio','Fecha_Finalizacion','S_Descripcion','S_Documentacion','S_Imagen','T_Fase_proyecto','T_Gestion','T_Tipo_Proyecto','T_Materia']
        widgets = {
            'Fecha_Inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'Fecha_Finalizacion': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(T_ProyectosForm, self).__init__(*args, **kwargs)
        settings = GlobalSettings.objects.first()
        if settings:
            hoy = date.today()
            if not (settings.fecha_inicio_habilitacion <= hoy <= settings.fecha_fin_habilitacion):
                for field in self.fields:
                    self.fields[field].disabled = True
                    
                

class GlobalSettingsForm(forms.ModelForm):
    class Meta:
        model = GlobalSettings
        fields = ['habilitar_proyectos','fecha_inicio_habilitacion', 'fecha_fin_habilitacion']
        widgets = {
            'fecha_inicio_habilitacion': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_fin_habilitacion': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(GlobalSettingsForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio_habilitacion'].input_formats = ['%Y-%m-%d']
        self.fields['fecha_fin_habilitacion'].input_formats = ['%Y-%m-%d']