from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class cajeros (models.Model):

    def __str__(self):
        return f"{self.nombre} --- {self.apellido} --- {self.tipo}"
    
    nombre = models.CharField (max_length = 25)
    apellido = models.CharField (max_length = 25)
    dni = models.IntegerField ()
    mail = models.EmailField ()
    localidad = models.CharField (max_length = 15)
    provincia = models.CharField (max_length = 15)
    tipo = models.CharField (max_length = 15)
    telefono = models.IntegerField ()


class fichas (models.Model):
    
    def __str__(self):
        return f"{self.cajero} --- {self.cantidad} --- {self.porcentaje}"
 
    cajero = models.CharField (max_length = 25)
    cantidad = models.IntegerField ()
    precio = models.IntegerField ()
    porcentaje = models.IntegerField ()


class ventas (models.Model):

    def __str__(self):
        return f"{self.cajeros} --- {self.mes} --- {self.fichas_vendidas} --- {self.premios} "

    cajeros = models.CharField (max_length = 25)
    mes = models.CharField (max_length = 15)
    fichas_vendidas = models.IntegerField ()
    premios = models.IntegerField ()

class premios (models.Model):
    def __str__(self):
       return f"{self.cajeron} --- {self.nombreu} --- {self.importe} --- {self.cvu} "

    cajeron = models.CharField (max_length = 25)
    nombreu = models.CharField (max_length = 25)
    importe = models.IntegerField ()
    cvu = models.CharField (max_length = 35)
    
class avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    imagen = models.ImageField(cajeros,upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"





