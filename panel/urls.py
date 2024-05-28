from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hometrabajos', views.hometrabajos, name='hometrabajos'),
    path('repoin', views.repoin, name='repoin'),
    path('repoti', views.repoti, name='repoti'),
    #logueamiento
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]