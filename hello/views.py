# blog/views.py
from django.views.generic.list import ListView
from django.shortcuts import render



from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'inicio.html'


def index(request):
     return render(request, 'inicio.html')

def cronograma1(request):
     return render(request, 'cronograma1.html')

def cronograma2(request):
     return render(request, 'cronograma2.html')

def materiais(request):
     return render(request, 'materiais.html')

def relatorios(request):
     return render(request, 'relatorios.html')

def dashboard(request):
     return render(request, 'dashboard.html')
