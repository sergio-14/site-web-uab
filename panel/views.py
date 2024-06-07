from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import ProyectoForm, CommentForm, PersonaForm, T_ProyectosForm, GlobalSettings, GlobalSettingsForm
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Proyecto, Commentario, Persona, T_Proyectos, T_Gestion, T_Semestre
from panel.models import Proyecto
from django.contrib.auth.models import User

from django.views.generic import View


from django.core.mail import send_mail


#inicio
def home(request):
    return render(request, 'home.html')

# vista de acceso publico
def hometrabajos(request):
    return render(request, 'homesocial/hometrabajos.html')


#poryectos interacion social
def repoin(request):
    t_gestion_id = request.GET.get('T_Gestion')
    t_semestre_id = request.GET.get('T_Semestre')
    
    # Inicializar listaproyectos como vacío
    listaproyectos = T_Proyectos.objects.none()
    
    if t_gestion_id or t_semestre_id:
        listaproyectos = T_Proyectos.objects.all()
        
        if t_gestion_id:
            listaproyectos = listaproyectos.filter(T_Gestion_id=t_gestion_id)
        
        if t_semestre_id:
            listaproyectos = listaproyectos.filter(T_Materia__T_Semestre_id=t_semestre_id)
        
        listaproyectos = listaproyectos.order_by('Id_Proyect')  # Ordenar para garantizar el primer proyecto
    
    # Obtener el primer proyecto si existe, de lo contrario None
    primer_proyecto = listaproyectos.first() if listaproyectos.exists() else None
    
    context = {
        'primer_proyecto': primer_proyecto,
        't_gestiones': T_Gestion.objects.all(),
        't_semestres': T_Semestre.objects.all(),
        'listaproyectos': listaproyectos,
        'selected_t_gestion': t_gestion_id,
        'selected_t_semestre': t_semestre_id,
    }
    
    return render(request, 'homesocial/repoin.html', context)


def repoti(request):
    return render(request, 'homesocial/repoti.html')

# .volver a home al cerrar sesion
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Usuario y/o contraseña incorrectos."
            return render(request, 'signin.html', {'error_message': error_message})
    return render(request, 'signin.html')

@login_required
def dashboard(request):
    dashboard_url = reverse('dashboard')  # Obtiene la URL inversa para la vista 'dashboard'
    return render(request, 'dashboard.html', {'dashboard_url': dashboard_url})



@permission_required('seguimiento.can_view_custom_view')
def editar_persona(request):
    # Obtener la persona asociada al usuario que inició sesión
    persona = get_object_or_404(Persona, user=request.user)

    if request.method == 'POST':
        formE = PersonaForm(request.POST, request.FILES, instance=persona)
        if formE.is_valid():
            formE.save()
            return redirect('detalle_persona')
    else:
        formE = PersonaForm(instance=persona)
    
    return render(request, 'usuarios/editar_persona.html', {'formE': formE})

@login_required
def detalle_persona(request):
    # Obtener la persona asociada al usuario que inició sesión
    personav = get_object_or_404(Persona, user=request.user)
    return render(request, 'usuarios/detalle_persona.html', {'personav': personav})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        destinatario_id = request.POST.get('destinatario')
        destinatario = User.objects.get(id=destinatario_id)
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        # Envía el correo electrónico
        send_mail(asunto, mensaje, 'shuerkk.14@gmail.com', [destinatario.email])

        return redirect('dashboard')

    # Obtener todos los usuarios excepto el usuario actual
    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'enviar_mensaje.html', {'usuarios': usuarios})


def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            # Generar un slug único para el proyecto
            slug = slugify(proyecto.titulo)
            counter = 1
            while Proyecto.objects.filter(slug=slug).exists():
                slug = f"{slug}-{counter}"
                counter += 1
            proyecto.slug = slug
            # Asignar la Persona asociada al usuario actual
            proyecto.persona = request.user.persona
            proyecto.save()
            return redirect('dashboard')
    else:
        form = ProyectoForm()
    return render(request, 'agregar_proyecto.html', {'form': form})

@login_required
def vista_proyecto(request):
    # Obtener todos los proyectos asociados al usuario en sesión
    proyectos_usuario = Proyecto.objects.filter(persona=request.user.persona).order_by('-fecha_creacion')

    # Paginación
    paginator = Paginator(proyectos_usuario, 1)  # Mostrar un proyecto por página
    page_number = request.GET.get('page')
    proyectos_paginados = paginator.get_page(page_number)

    return render(request, 'proyectos/vista_proyecto.html', {'proyectos': proyectos_paginados})

def agregar_comentario(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        formf = CommentForm(request.POST)
        if formf.is_valid():
            comentario = formf.save(commit=False)
            comentario.proyecto_relacionado = proyecto
            comentario.user = request.user  # Asigna el usuario actual
            comentario.save()
            return redirect('dashboard', proyecto_id=proyecto_id)
    else:
        formf = CommentForm()
    return render(request, 'proyectos/agregar_comentario.html', {'formf': formf, 'proyecto': proyecto})

# Esta clase maneja la vista para mostrar proyectos pendientes de aprobación 
# y permitir la adición de comentarios a dichos proyectos.

#permisos
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator   
from django.core.exceptions import PermissionDenied  


# Define la función de verificación de permisos aquí para usuarios
def usuario_en_grupo(user, grupoestudiantes):
    try:
        grupo = Group.objects.get(name=grupoestudiantes)
    except Group.DoesNotExist:
        raise PermissionDenied(f"El grupo '{grupoestudiantes}' no existe.")
    
    if grupo in user.groups.all():
        return True
    else:
        raise PermissionDenied
    
def handle_permission_denied(request, exception):
    return render(request, '403.html', status=403)


@method_decorator(user_passes_test(lambda u: usuario_en_grupo(u, 'grupoestudiantes')), name='dispatch')
class ProyectosParaAprobar(View):
    def get(self, request):
        proyectos = Proyecto.objects.filter(estado='Pendiente')
        proyectos_con_formulario = {proyecto: CommentForm() for proyecto in proyectos}
        
        context = {
            'proyectos': proyectos_con_formulario,
        }
        return render(request, 'proyectos/ProyectosParaAprobar.html', context)
    
    def post(self, request):
        proyecto_id = request.POST.get('proyecto_id')
        comentario_texto = request.POST.get('comentario_texto')
        if proyecto_id and comentario_texto:
            proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
            Commentario.objects.create(comentari=comentario_texto, user=request.user, proyecto_relacionado=proyecto)
            messages.success(request, 'Comentario agregado exitosamente.')
        else:
            messages.error(request, 'Hubo un error al agregar el comentario.')
        
        if 'aprobar' in request.POST:
            return AprobarProyecto().post(request, proyecto_id)
        elif 'rechazar' in request.POST:
            return RechazarProyecto().post(request, proyecto_id)
        else:
            messages.error(request, 'Hubo un error al procesar la solicitud.')
            return HttpResponseRedirect(request.path_info)

class AprobarProyecto(View):
    def post(self, request, proyecto_id):
        proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
        proyecto.estado = 'Aprobado'
        proyecto.save()
        messages.success(request, '¡Proyecto aprobado exitosamente!')
        return HttpResponseRedirect(reverse('ProyectosParaAprobar'))

class RechazarProyecto(View):
    def post(self, request, proyecto_id):
        proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
        proyecto.estado = 'Rechazado'
        proyecto.save()
        messages.error(request, '¡Proyecto rechazado!')
        return HttpResponseRedirect(reverse('ProyectosParaAprobar'))


from datetime import date
#proyectos de interaccion social 
def proyecto_detail(request):
    settings = GlobalSettings.objects.first()
    hoy = date.today()
    habilitado = settings and (settings.fecha_inicio_habilitacion <= hoy <= settings.fecha_fin_habilitacion)
    tiempo_restante = settings.tiempo_restante() if settings else None

    if request.method == 'POST':
        form = T_ProyectosForm(request.POST, request.FILES)
        if habilitado and form.is_valid():
            proyecto = form.save(commit=False)  # No guardar todavía la instancia del modelo
            proyecto.S_persona = Persona.objects.get(user=request.user)  # Asignar la persona relacionada con el usuario autenticado
            proyecto.save()  # Ahora guardar la instancia del modelo
            return redirect('dashboard')  # Asegúrate de que 'dashboard' sea el nombre correcto de tu vista para el dashboard
    else:
        form = T_ProyectosForm()

    return render(request, 'homesocial/proyecto_detail.html', {
        'form': form,
        'habilitado': habilitado,
        'tiempo_restante': tiempo_restante,
    })

   
def lista_proyectos(request):
    proyectos = T_Proyectos.objects.all()
    return render(request, 'homesocial/lista_proyectos.html', {'proyectos': proyectos})


def global_settings_view(request):
    settings = GlobalSettings.objects.first()
    if not settings:
        settings = GlobalSettings()

    if request.method == 'POST':
        form = GlobalSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GlobalSettingsForm(instance=settings)
    
    return render(request, 'homesocial/global_settings.html', {'form': form})


@login_required
def proyectosin_so(request):
    persona = request.user.persona
    proyectos = T_Proyectos.objects.filter(S_persona=persona).order_by('-Id_Proyect')
    
    # Paginación para los proyectos, incluyendo el último proyecto
    paginator = Paginator(proyectos, 1)  # Muestra 1 proyecto por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'persona': persona,
        'page_obj': page_obj
    }
    return render(request, 'homesocial/proyectosin_so.html', context)