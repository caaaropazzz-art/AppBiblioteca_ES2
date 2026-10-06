from django.urls import path
from . import views

urlpatterns =[
    path('', views.lista_libros, name = 'lista_libros'),
    path('crear/', views.crear_libro, name= 'crear_libro'),
]