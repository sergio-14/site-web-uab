from django.apps import AppConfig


class PanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'panel'
    
    def ready(self):
        import panel.signals
        # Mueve la importación de User dentro de esta función
        from django.contrib.auth.models import User
