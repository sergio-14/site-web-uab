# en permissions.py de tu aplicación
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from .models import Proyecto

#content_type = ContentType.objects.get_for_model(Proyecto)
#Permission.objects.filter(
#    Q(codename='puede_aprobar_proyectos') |
#    Q(codename='puede_rechazar_proyectos')
#).delete()

#permiso_aprobar = Permission.objects.create(
#    codename='puede_aprobar_proyectos',
#    name='Puede aprobar proyectos',
#    content_type=content_type,
#)

#permiso_rechazar = Permission.objects.create(
#    codename='puede_rechazar_proyectos',
#    name='Puede rechazar proyectos',
#    content_type=content_type,
#)