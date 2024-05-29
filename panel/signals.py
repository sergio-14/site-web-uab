from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Proyecto, Persona

@receiver(pre_save, sender=Proyecto)
def asignar_persona(sender, instance, **kwargs):
    if not instance.persona_id:
        user = instance.persona.user if hasattr(instance, 'persona') else None
        if user:
            persona, created = Persona.objects.get_or_create(user=user)
            instance.persona = persona