from django.urls import path
from . import views
from django.conf.urls import handler403
from .views import handle_permission_denied

urlpatterns = [
    path('', views.home, name='home'),
    path('hometrabajos', views.hometrabajos, name='hometrabajos'),
    path('repoin', views.repoin, name='repoin'),
    path('repoti', views.repoti, name='repoti'),
    #logueamiento
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    
    
    #seguimiento
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agregar_proyecto/',views.agregar_proyecto, name='agregar_proyecto'),
    path('proyectos/vista_proyecto/',views.vista_proyecto, name='vista_proyecto'),
    path('proyecto/<int:proyecto_id>/comentario/agregar/', views.agregar_comentario, name='agregar_comentario'),
    
    #usuarios
    path('usuarios/editar_persona/', views.editar_persona, name='editar_persona'),
    path('usuarios/detalle_persona/', views.detalle_persona, name='detalle_persona'),
    #proyectos para aprobar
    path('proyectos/ProyectosParaAprobar/', views.ProyectosParaAprobar.as_view(), name='ProyectosParaAprobar'),
    path('AprobarProyecto/<int:proyecto_id>/', views.AprobarProyecto.as_view(), name='AprobarProyecto'),
    path('RechazarProyecto/<int:proyecto_id>/', views.RechazarProyecto.as_view(), name='RechazarProyecto'),
    
    #mensajes correo
    path('enviar-mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    
    
    #proyectos de interacion social
    path('homesocial/proyecto_detail/', views.proyecto_detail, name='proyecto_detail'),
    path('homesocial/global_settings/', views.global_settings_view, name='global_settings'),
    path('homesocial/proyectosin_so/', views.proyectosin_so, name='proyectosin_so'),
    
]
handler403 = handle_permission_denied
