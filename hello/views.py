
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect



def index(request):
     return render(request, 'inicio.html')

@login_required(login_url='/accounts/login/')
def menu(request):
     return render(request, 'menu.html')

@login_required(login_url='/accounts/login/')
def cronograma1(request):
     return render(request, 'cronograma1.html')

@login_required(login_url='/accounts/login/')
def cronograma2(request):
     return render(request, 'cronograma2.html')

@login_required(login_url='/accounts/login/')
def materiais(request):
     return render(request, 'materiais.html')

@login_required(login_url='/accounts/login/')
def relatorios(request):
     return render(request, 'relatorios.html')

@login_required(login_url='/accounts/login/')
def dashboard(request):
     return render(request, 'dashboard.html')
