from django.contrib import admin
from django.urls import path
from libros import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Usa la vista de logout personalizada
    path('registrarse/', views.registrar, name='registrarse'),  # URL para el registro
    path('', views.lista_libros, name='lista_libros'),
    path('libro/nuevo/', views.crear_libro, name='crear_libro'),
    path('libro/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libro/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
