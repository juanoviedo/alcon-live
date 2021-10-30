from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import datetime

from main.forms import CreateNewClient
from .models import Client, Day
# Create your views here.


def client(response, id):
    cli = Client.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            fecha = response.POST.get("fecha")
            vacas = response.POST.get("vacas")
            concentrado = response.POST.get("concentrado")
            leche = response.POST.get("leche")

            datem = datetime.datetime.strptime(fecha, "%Y-%m-%d")

            if int(vacas) > 2 and int(concentrado) > -1 and int(leche) > 0 and datem.year > 2000 and datem.year < 2100:
                cli.day_set.create(date=fecha, totalcows=vacas, animalfeed=concentrado, totalmilk=leche)
            else:
                print("invalid input")
            

    return render(response, "main/client.html", {"cli":cli})

def create(response):
    if response.method == "POST":
        form = CreateNewClient(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Client(name=n)
            t.save()

        return HttpResponseRedirect("/client/%i" %t.id)

    else:
        cli = Client.objects
        form = CreateNewClient()

    return render(response, "main/create.html", {"form":form, "cli":cli})

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

