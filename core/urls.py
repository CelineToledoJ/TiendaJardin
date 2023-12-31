"""
URL configuration for TIENDAJARDIN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('addtocar2/<codigo>', addtocar2, name="addtocar2"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('limpiar', limpiar),
    path('catalogo', catalogo, name="catalogo"),
    path('comprar', comprar, name="comprar"),    
    path('fundacion', fundacion, name="fundacion"),
    path('carrito', carrito, name="carrito"),
    path('envios', envios, name="envios"),
    path('suscribir', suscribir, name="suscribir"),
]
