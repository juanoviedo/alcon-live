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

            if int(vacas) > 2 and int(concentrado) > -1 and int(leche) > 0 and datem.year > 2000 and datem.year < 2100:

                lechevaca = leche/vacas
                eficiencia = leche/concentrado
                conversion = concentrado/leche

                if eficiencia > 20:
                    estado = "success"
                    obser = "Tu día fue muy productivo!"

                elif eficiencia < 20 and eficiencia > 15:
                    estado = "warning"
                    obser = "Tu estuvo bien pero puede mejorar"
                else:
                    estado = "danger"
                    obser = "Tu día no fue muy productivo, debes revisar en que puedes mejorar"

                datem = datetime.datetime.strptime(fecha, "%Y-%m-%d")

                cli.day_set.create(date=fecha, cows=vacas, milk=leche, feed=concentrado, cowmilk=lechevaca, efficiency=eficiencia, conversion=conversion, status=estado, obs=obser)
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

