from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import login as auth_login  
from django.contrib.auth import logout
from django.contrib import messages  
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El libro ha sido creado exitosamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "El libro ha sido actualizado exitosamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, "El libro ha sido eliminado exitosamente.")
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('lista_libros')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'libros/login.html', {'form': form})

def logout_view(request):
    logout(request)  
    messages.success(request, "Has cerrado sesión correctamente.")  
    return redirect('login') 

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Te has registrado exitosamente!")
            return redirect('login')  
    else:
        form = UserCreationForm()
    
    return render(request, 'libros/registro.html', {'form': form})