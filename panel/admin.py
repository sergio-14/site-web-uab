from django.contrib import admin

# Register your models here.
from panel.models import Persona,Categoria,Proyecto, Commentario
admin.site.register(Persona)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Commentario)

