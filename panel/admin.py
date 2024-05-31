from django.contrib import admin

# Register seguimiento
from panel.models import Persona,Categoria,Proyecto, Commentario
admin.site.register(Persona)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Commentario)


from .models import T_Fase_proyecto, T_Tipo_Proyecto, T_Gestion, T_Proyectos, T_Semestre, T_Materia

# Register interacion social
admin.site.register(T_Fase_proyecto)
admin.site.register(T_Tipo_Proyecto)
admin.site.register(T_Gestion)
admin.site.register(T_Proyectos)
admin.site.register(T_Semestre)
admin.site.register(T_Materia)


