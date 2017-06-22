from django.conf.urls import url
from . import views

def index(request):

    return render(request, './form/templates/index.html', context)

def detail(request):

    return render(request, './form/templates/snippets.html', context)

def add(request):

    return render(request, 'users/add.html', context)
