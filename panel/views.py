from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


#inicio
def home(request):
    return render(request, 'home.html')

# vista de acceso publico
def hometrabajos(request):
    return render(request, 'homesocial/hometrabajos.html')

def repoin(request):
    return render(request, 'homesocial/repoin.html')

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
            return redirect('home')
        else:
            error_message = "Usuario y/o contraseña incorrectos."
            return render(request, 'signin.html', {'error_message': error_message})
    return render(request, 'signin.html')