from django.shortcuts import render, redirect
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def crear_libro(request):

    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        isbn = request.POST['isbn']
        fecha_publicacion = request.POST['fecha_publicacion']
        disponible = 'disponible' in request.POST

        Libro.objects.create(
            titulo = titulo,
            autor = autor,
            isbn = isbn,
            fecha_publicacion = fecha_publicacion,
            disponible = disponible
        )

        return redirect('lista_libros')

    return render(request, 'libros/crear_libro.html')