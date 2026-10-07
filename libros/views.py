from django.shortcuts import render, redirect, get_object_or_404
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

def editar_libro(request, id):

    libro = Libro.objects.get(id=id)

    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.isbn = request.POST['isbn']
        libro.fecha_publicacion = request.POST['fecha_publicacion']
        libro.disponible = 'disponible' in request.POST

        libro.save()

        return redirect('lista_libros')

    return render(request, 'libros/editar_libro.html', {'libro': libro})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
        
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})