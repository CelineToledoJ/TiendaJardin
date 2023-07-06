from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    estado = models.CharField(max_length=20, default="EN PREPARACION")
    

    def __str__(self):
        return str(self.id)+ str(self.fecha)[0:16]


class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    porcentaje = models.IntegerField()
    imagen = models.CharField(max_length=200)


    def tachado(self):
        if self.oferta:
            return "Antes $"+str(round((self.precio * self.porcentaje)/100)+ self.precio)+" - Ahora"
        return ""
    
    def __str__(self):
        return self.detalle+" ("+self.codigo+")"
    
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200, default="https://i.kym-cdn.com/entries/icons/facebook/000/038/239/maxresdefault.jpg")

    def __str__(self):
        return str(self.id)+" "+self.producto.codigo
    
