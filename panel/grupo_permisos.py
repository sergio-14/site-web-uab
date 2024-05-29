
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='en_grupo')
def en_grupo(user, grupoestudiantes):
    grupo = Group.objects.get(name=grupoestudiantes)
    return grupo in user.groups.all()