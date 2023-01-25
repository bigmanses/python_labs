from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'newsApp/index.html', data)

def about(request):
    return render(request, 'newsApp/about.html')
