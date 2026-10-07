from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from datetime import date

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo'].strip()
        autor = request.POST['autor'].strip()
        isbn = request.POST['isbn'].strip()
        fecha_publicacion = request.POST['fecha_publicacion']
        disponible = 'disponible' in request.POST
        if titulo == '' or autor == '' or isbn == '' or fecha_publicacion == '':
            return render(request, 'libros/crear_libro.html', {
                'error': 'Todos los campos son obligatorios.'
            })
        if len(titulo) > 200:
            return render(request, 'libros/crear_libro.html', {
                'error': 'El título no puede superar los 200 caracteres.'
            })
        if len(autor) > 150:
            return render(request, 'libros/crear_libro.html', {
                'error': 'El autor no puede superar los 150 caracteres.'
            })
        if not isbn.isdigit():
            return render(request, 'libros/crear_libro.html', {
                'error': 'El ISBN debe contener solo números.'
            })
        if len(isbn) not in [10, 13]:
            return render(request, 'libros/crear_libro.html', {
                'error': 'El ISBN debe tener 10 o 13 dígitos.'
            })
        if fecha_publicacion > str(date.today()):
            return render(request, 'libros/crear_libro.html', {
                'error': 'La fecha de publicación no puede ser futura.'
            })
        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            fecha_publicacion=fecha_publicacion,
            disponible=disponible
        )
        return redirect('lista_libros')
    return render(request, 'libros/crear_libro.html')

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)

    if request.method == "POST":
        titulo = request.POST['titulo'].strip()
        autor = request.POST['autor'].strip()
        isbn = request.POST['isbn'].strip()
        fecha_publicacion = request.POST['fecha_publicacion']
        disponible = 'disponible' in request.POST

        if titulo == '' or autor == '' or isbn == '' or fecha_publicacion == '':
            return render(request, 'libros/editar_libro.html', {'error': 'Todos los campos son obligatorios.'})

        if len(titulo) > 200:
            return render(request, 'libros/editar_libro.html', {'error': 'El título no puede superar los 200 caracteres.'})

        if len(autor) > 150:
            return render(request, 'libros/editar_libro.html', {'error': 'El autor no puede superar los 150 caracteres.'})

        if not isbn.isdigit():
            return render(request, 'libros/editar_libro.html', {'error': 'El ISBN debe contener solo números.'})

        if len(isbn) not in [10, 13]:
            return render(request, 'libros/editar_libro.html', {'error': 'El ISBN debe tener 10 o 13 dígitos.'})

        if fecha_publicacion > str(date.today()):
            return render(request, 'libros/editar_libro.html', {'error': 'La fecha de publicación no puede ser futura.'})

        libro.titulo = titulo
        libro.autor = autor
        libro.isbn = isbn
        libro.fecha_publicacion = fecha_publicacion
        libro.disponible = disponible
        libro.save()

        return redirect('lista_libros')

    return render(request, 'libros/editar_libro.html', {'libro': libro})

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
        
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})