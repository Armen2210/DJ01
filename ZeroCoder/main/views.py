from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'caption': 'Генератор Django'})

def new(request):
    return render(request, 'main/new.html', {'caption': 'Генератор Django'})

def data(request):
    return render(request, 'main/data.html', {'caption': 'Генератор Django'})

def test(request):
    return render(request, 'main/test.html', {'caption': 'Генератор Django'})
