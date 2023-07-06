from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
import requests
# Create your views here.


def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break 
    else:
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1 , producto.precio])
    request.session["carro"] = carro
    return redirect (to="catalogo")

def addtocar2(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break 
    else:
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1 , producto.precio,])
    request.session["carro"] = carro
    return redirect (to="carrito")
    

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break 
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect (to="carrito")


def limpiar(request):
    request.session.flush()
    return redirect(to="catalogo")

def home(request):
    return render(request, 'core/index.html')


def login(request):
    return render(request, 'core/login.html')

def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form': registro})


def catalogo(request):
    plantas = Producto.objects.all()
    return render(request, 'core/catalogo.html', {'plantas': plantas, "carro":request.session.get("carro", [])})


def fundacion(request):
    return render(request, 'core/fundacion.html')

def carrito(request):
    return render(request, 'core/carrito.html', {"carro":request.session.get("carro", [])})


def comprar(request):
    carro = request.session.get("carro", [])
    total = 0
    for c in carro:
        total += c[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    # Guardamos cada producto en la tabla detalle
    for c in carro:
        producto = Producto.objects.get(codigo=c[0])
        imagen = Producto.objects.get(imagen= c[2])
        detalle = DetalleVenta()
        detalle.venta = venta
        detalle.imagen = imagen
        detalle.producto = producto
        detalle.cantidad = c[4]
        detalle.precio = c[3]
        detalle.total = c[5]
        detalle.save()
        producto.stock = producto.stock - c[4]
        producto.save()
    request.session["carro"] = []
    return redirect(to="carrito")


def envios(request):
        ventas = Venta.objects.filter(cliente=request.user)
        return render(request, 'core/envios.html', {"ventas":ventas})








def suscribir(request):
    context = {}
    suscrito(request, context)
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
        return render(request, 'core/fundacion.html', context)
    else:
        return render(request, 'core/fundacion.html', context)

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]



