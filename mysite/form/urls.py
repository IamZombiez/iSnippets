from django.conf.urls import url
from . import views

def index(request):

    return render(request, 'users/index.html', context)

def detail(request):

    return render(request, 'users/snippets.html', context)

def add(request):

    return render(request, 'users/codeform.html', context)
