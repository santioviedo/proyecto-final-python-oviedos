from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User 

class cajerosformulario (forms.Form):
    nombre = forms.CharField (max_length = 25)
    apellido = forms.CharField (max_length = 25)
    dni = forms.IntegerField ()
    mail = forms.EmailField ()
    localidad = forms.CharField (max_length = 15)
    provincia = forms.CharField (max_length = 15)
    tipo = forms.CharField (max_length = 15)
    telefono = forms.IntegerField ()


class fichasformulario (forms.Form):
    cajero = forms.CharField (max_length = 25)
    cantidad = forms.IntegerField ()
    precio = forms.IntegerField ()
    porcentaje = forms.IntegerField ()


class ventasformulario (forms.Form):
    cajeros = forms.CharField (max_length = 25)
    mes = forms.CharField (max_length = 15)
    fichas_vendidas = forms.IntegerField ()
    premios = forms.IntegerField ()

class premiosformulario (forms.Form):
    cajeron = forms.CharField (max_length = 25)
    nombreu = forms.CharField (max_length = 25)
    importe = forms.IntegerField ()
    cvu = forms.IntegerField ()

class RegistrarUsuarios(UserChangeForm):
    email = forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="Ingrese la Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme la Contraseña",widget=forms.PasswordInput)
    last_name = forms.CharField(label="Ingrese su Nombre")
    first_name = forms.CharField(label="Ingrese su Apellido")

    class Meta:
        model = User
        fields = ["username","email","password1","password2","last_name","first_name"]
    

