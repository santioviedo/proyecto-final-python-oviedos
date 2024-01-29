"""
URL configuration for proyectofinal project.

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
from django.contrib import admin
from django.urls import path
from Appcasino.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",inicio, name= "inicio"),
    path("nuevocajero/", agregar_cajeros, name="ncajero"),
    path("nuevaficha/", agregar_fichas, name="nficha"),
    path("nuevaventa/", agregar_ventas, name="nventa"),
    path("nuevopremio/", agregar_premios, name="npremio"),

    path("vercajeros/",vercajeros, name="vcajeros"),
    path("verfichas/",verfichas, name="vfichas"),
    path("verventas/",verventas, name="vventas"),
    path("verpremios/",verpremios, name="vpremios"),

    path("mostrarcajero/",mostrar_cajero, name = "mcajero"),
    path("mostrarficha/",mostrar_fichas, name = "mfichas"),
    path("mostrarpremios/",mostrar_premios, name = "mpremios"),
    path("mostrarventas/",mostrar_ventas, name = "mventas"),

    path("buscarpornombre/",busqueda_nombre, name= "buscar"),
    path("resultadonombre/",resultado_nombre, name= "resultado1"),

    path("actualizarcajero/<cajero_nombre>",actualizar_cajeros, name = "actualizarcajero"),
    path("actualizarfichas/<fichas_cajero>",actualizar_fichas, name = "actualizarficha"),
    path("actualizarventas/<ventas_cajeros>",actualizar_ventas, name = "actualizarventa"),
    path("actualizarpremios/<premios_cajeron>",actualizar_premios, name = "actualizarpremio"),

    path("eliminar/<cajero_nombre>", eliminar_cajero, name = "eliminarcajero"),

    path("login/",inicio_sesion, name="login"),


    path("registrarse/",registro, name="registro"),

    path("logout/", LogoutView.as_view(template_name="registro/cerrar_sesion.html"),name="cerrarsesion"),

    path("edit/",editar_perfil, name="editarusuario"),

    path("cambiarcajero/",cambiar_cajero, name = "actualizarcajero"),

]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)