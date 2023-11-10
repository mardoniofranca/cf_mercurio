from django.contrib import admin
from django.urls import path, include
admin.autodiscover()

import hello.views

urlpatterns = [
    path('admin/', admin.site.urls),        
    path('accounts/', include('django.contrib.auth.urls')),
    path('',hello.views.index,name="home"),
    path('menu/',hello.views.menu,name="menu"),
    path('cronograma1/',hello.views.cronograma1,name='cronograma1'),
    path('cronograma2/',hello.views.cronograma2,name='cronograma2'),
    path('materiais/',hello.views.materiais,name='materiais'),
    path('relatorios/',hello.views.relatorios,name='relatorios'),
    path('dashboard/',hello.views.dashboard,name='dashboard'),
   
]

