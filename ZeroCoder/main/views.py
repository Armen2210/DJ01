from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'caption': 'Генератор Django'})

def new(request):
    return render(request, 'main/new.html', {'caption': 'Генератор Django'})

def data(request):
    return HttpResponse("<h1>Это страница data</h1>")

def test(request):
    return HttpResponse("<h1>Это страница test</h1>")
