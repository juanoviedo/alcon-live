from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})

def ganado(response):
    return render(response, "main/ganado.html", {})