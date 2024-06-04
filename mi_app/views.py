from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, EditorialForm
from .models import Libro

def home (request):
    return render(request, 'home.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_editorial')
    else:
        form = EditorialForm()
    return render(request, 'crear_editorial.html', {'form': form})

def buscar_libro(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=query)
        return render(request, 'buscar_libro.html', {'libros': libros, 'query': query})
    return render(request, 'buscar_libro.html')
