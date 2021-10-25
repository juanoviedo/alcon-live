from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})

def avicultura(response):
    return render(response, "main/avicultura.html", {})

def equinos(response):
    return render(response, "main/equinos.html", {})

def ganaderia(response):
    return render(response, "main/ganaderia.html", {})

def porcicultura(response):
    return render(response, "main/porcicultura.html", {})

def mascotas(response):
    return render(response, "main/mascotas.html", {})

def cunicultura(response):
    return render(response, "main/cunicultura.html", {})

def acuicultura(response):
    return render(response, "main/acuicultura.html", {})

def vidinst(response):
    return render(response, "main/vidinst.html", {})

def puntosventa(response):
    return render(response, "main/puntosventa.html", {})

def contactenos(response):
    return render(response, "main/contactenos.html", {})