from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return render(request, 'templaa.html')


def sobre(request):
    return render(request, 'recipes/sobre.html')


def teste(request):
    return render(request, 'temp/tempp.html')
