"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views 
# URL Login
from django.contrib.auth import views as auth


urlpatterns = [
    
    path('admin/', admin.site.urls), # solo entran los superusuarios
    #1 parámetros en el texto de la URL
    #2 Vista que se va a ejectutar
    #3 Es el nombre de la URL
    path('', views.Home, name = 'home'), # '' -- >queda vacío porque no hay nada después de la /, si pongo AA, aparecerá Noticias/AA

    # NO necesariamente estos tres valores se deben llamar igual ... url -> vista -> template

    path ('Nosotros/', views.Nosotros, name = 'nosotros' ),
    path ('quienes_somos/', views.somos, name = 'quienes_somos' ),  

    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),


    # url de aplicación
    path('Noticias/', include ('apps.noticias.urls')),
    path('Usuario/',include('apps.usuarios.urls'))

]
