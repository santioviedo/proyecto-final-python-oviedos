from django.shortcuts import render
from Appcasino.models import *
from Appcasino.form import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def inicio (request):
    return render (request, "inicio.html")

def vercajeros (request):
    return render (request,"vercajeros.html")

def verfichas (request):
    return render (request,"verfichas.html")

def verpremios (request):
    return render (request,"verpremios.html")

def verventas (request):
    return render (request,"verventas.html")




@login_required
def agregar_cajeros(request):

    if request.method=="POST":
        info_formulario = cajerosformulario (request.POST)

        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            cajero1 = cajeros (nombre=info["nombre"],apellido=info["apellido"],dni=info["dni"],
                               mail=info["mail"],localidad=info["localidad"],provincia=info["provincia"],
                               tipo=info["tipo"],telefono=info["telefono"],)
            cajero1.save()
            return render (request,"inicio.html")
    else:    

        info_formulario = cajerosformulario ()
    return render (request, "cajeros.html",{"formu":info_formulario})

@login_required
def agregar_fichas(request):

    if request.method=="POST":
         info_formulario = fichasformulario (request.POST)
 
         if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            fichas1 = fichas (cajero=info["cajero"],cantidad=info["cantidad"],precio=info["precio"],porcentaje=info["porcentaje"],)
            fichas1.save()
            return render (request,"inicio.html")
    else:    

          info_formulario = fichasformulario ()
    return render (request, "fichas.html",{"formu":info_formulario})

@login_required
def agregar_ventas(request):

    if request.method=="POST":
         info_formulario = ventasformulario (request.POST)

         if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            ventas1 = ventas (cajeros=info["cajeros"],mes=info["mes"],fichas_vendidas=info["fichas_vendidas"],premios=info["premios"],)
            ventas1.save()
            return render (request,"inicio.html")
    else:    

          info_formulario = ventasformulario ()
    return render (request, "ventas.html",{"formu":info_formulario})

@login_required
def agregar_premios(request):

    if request.method=="POST":
         info_formulario = premiosformulario (request.POST)

         if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            premios1 = premios (cajeron=info["cajeron"],nombreu=info["nombreu"],importe=info["importe"],cvu=info["cvu"],)
            premios1.save()
            return render (request,"inicio.html")
    else:    

          info_formulario = premiosformulario ()
    return render (request, "premios.html",{"formu":info_formulario})

#------------------------------------------------------------------------------------------------------------------------------------

@login_required
def mostrar_cajero (request): 
    mis_cajeros = cajeros.objects.all()
    info = {"cajeros":mis_cajeros}
    return render (request, "mostrarcajero.html",info)
    
    
@login_required
def mostrar_fichas (request): 
    mis_fichas = fichas.objects.all()
    info = {"fichas":mis_fichas}
    return render (request, "mostrarfichas.html",info)

@login_required
def mostrar_premios (request): 
    mis_premios = premios.objects.all()
    info = {"premios":mis_premios}
    return render (request, "mostrarpremios.html",info)

@login_required
def mostrar_ventas (request): 
    mis_ventas = ventas.objects.all()
    info = {"ventas":mis_ventas}
    return render (request, "mostrarventas.html",info)

#------------------------------------------------------------------------------------------------------------------------------------

def busqueda_nombre(request):
    return render (request,"inicio.html")

def resultado_nombre(request):
    if request.GET["nombres"]:
        nombre= request.GET["nombres"]
        apellidos=cajeros.objects.filter(nombre__icontains=nombre)
        return render(request, "inicio.html", {"apellidos":apellidos, "nombre":apellidos})
    else:
        return render(request,"buscarnombre.html")

#-------------------------------------------------------------------------------------------------------------------------------------

    
def actualizar_cajeros(request,cajero_nombre):
     
    cajero_elegido =  cajeros.objects.get(nombre=cajero_nombre)

    if request.method=="POST":
        info_formulario = cajerosformulario(request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data

            cajero_elegido.nombre = info ["nombre"]
            cajero_elegido.apellido = info ["apellido"]
            cajero_elegido.dni = info ["dni"]
            cajero_elegido.mail = info ["mail"]
            cajero_elegido.localidad = info ["localidad"]
            cajero_elegido.provincia = info ["provincia"]
            cajero_elegido.tipo = info ["tipo"]
            cajero_elegido.telefono = info ["telefono"]
            cajero_elegido.save()

            return render (request,"inicio.html")
    else:    

        info_formulario = cajerosformulario (initial={"nombre":cajero_elegido.nombre, "apellido":cajero_elegido.apellido, "dni":cajero_elegido.dni,
                                                       "mail":cajero_elegido.mail, "localidad":cajero_elegido.localidad, "provincia":cajero_elegido.provincia,
                                                        "tipo":cajero_elegido.tipo, "telefono":cajero_elegido.telefono })
    return render (request, "actualizar_cajero.html",{"formu":info_formulario})


def actualizar_fichas(request,fichas_cajero):
     
    fichas_elegidas =  fichas.objects.get(cajero=fichas_cajero)

    if request.method=="POST":
        info_formulario = fichasformulario(request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data

            fichas_elegidas.cajero = info ["cajero"]
            fichas_elegidas.cantidad = info ["cantidad"]
            fichas_elegidas.precio = info ["precio"]
            fichas_elegidas.porcentaje = info ["porcentaje"]
            fichas_elegidas.save()

            return render (request,"inicio.html")
    else:    

        info_formulario = fichasformulario (initial={"cajero":fichas_elegidas.cajero, "cantidad":fichas_elegidas.cantidad, "precio":fichas_elegidas.precio,  "porcentaje":fichas_elegidas.porcentaje, })
    return render (request, "actualizarfichas.html",{"formu":info_formulario})



def actualizar_ventas(request,ventas_cajeros):
     
    ventas_elegidas =  ventas.objects.get(cajeros=ventas_cajeros)

    if request.method=="POST":
        info_formulario = ventasformulario(request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data

            ventas_elegidas.cajeros = info ["cajeros"]
            ventas_elegidas.mes = info ["mes"]
            ventas_elegidas.fichas_vendidas = info ["fichas_vendidas"]
            ventas_elegidas.premios = info ["premios"]
            ventas_elegidas.save()

            return render (request,"inicio.html")
    else:    

        info_formulario = ventasformulario (initial={"cajeros":ventas_elegidas.cajeros, "mes":ventas_elegidas.mes, "fichas_vendidas":ventas_elegidas.fichas_vendidas,  "premios":ventas_elegidas.premios, })
    return render (request, "actualizarventas.html",{"formu":info_formulario})



def actualizar_premios(request,premios_cajeron):
     
    premios_elegidos =  premios.objects.get(cajeron=premios_cajeron)

    if request.method=="POST":
        info_formulario = premiosformulario(request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data

            premios_elegidos.cajeron = info ["cajeron"]
            premios_elegidos.nombreu = info ["nombreu"]
            premios_elegidos.importe = info ["importe"]
            premios_elegidos.cvu = info ["cvu"]
            premios_elegidos.save()

            return render (request,"inicio.html")
    else:    

        info_formulario = premiosformulario (initial={"cajeron":premios_elegidos.cajeron, "nombreu":premios_elegidos.nombreu, "importe":premios_elegidos.importet,  "cvu":premios_elegidos.cvu, })
    return render (request, "actualizarpremios.html",{"formu":info_formulario})






#---------------------------------------------------------------------------------------------------------------------------------------
@login_required
def eliminar_cajero(request,cajero_nombre):
    cajero_elegido = cajeros.objects.get(nombre=cajero_nombre)
    cajero_elegido.delete()
    return render (request, "vercajeros.html")
#----------------------------------------------------------------------------------------------------------------------------------------

def inicio_sesion(request):
    if request.method=="POST":
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            info=formulario.cleaned_data
            usuario = info["username"]
            contra = info["password"]

            usuario_actual =authenticate(username=usuario, password=contra)

            if usuario_actual is not None:
                login(request, usuario_actual)

            return render(request,"inicio.html",{"mensaje":f"Bienvenido {usuario}"} )
        
        else:
            return render (request, "registro/inicio_sesion.html", {"mensaje": f"ERROR, los Datos Ingresados son Incorrectos Vuelva a Iniciar"})
        
    else:
        formulario = AuthenticationForm()
        return render (request, "registro/inicio_sesion.html", {"formu":formulario} )

#----------------------------------------------------------------------------------------------------------------------------------------

def registro(request):

    if request.method == "POST":
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = info["username"]
            formulario.save()
            return render (request,"inicio.html", {"mensaje": f"bienvenido {usuario}"})
    else: 
        formulario = UserCreationForm()
    return render (request, "registro/registrar_usuario.html",{"formu":formulario})

#---------------------------------------------------------------------------------------------------------------------------------------

def editar_perfil(request):
    usuario_actual = request.user

    if request.method == "POST":
        formulario = RegistrarUsuarios(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario_actual.username = info["username"]
            usuario_actual.save()
            return render (request,"inicio.html",)
    else: 
        formulario = RegistrarUsuarios(initial={"first_name":usuario_actual.first_name, "last_name":usuario_actual.last_name, "email":usuario_actual.email})
    return render (request,"registro/editar_usuario.html",{"formu":formulario}) 

#----------------------------------------------------------------------------------------------------------------------------------------
@login_required
def cambiar_cajero (request): 
    mis_cajeros = cajeros.objects.all()
    info = {"cajeros":mis_cajeros}
    return render (request, "cambiarcajero.html",info)