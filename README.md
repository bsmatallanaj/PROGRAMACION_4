# PROGRAMACION_4
Repositorio para guardar los talleres de la clase de programación 4 ts7a.  

##  Proyecto: Biblioteca en Django  

### Descripción General  
Biblioteca en Django es una aplicación web diseñada para gestionar libros de manera eficiente y amigable. Este proyecto académico está enfocado en el manejo de libros y usuarios, con las siguientes características principales:  
- CRUD (Crear, Leer, Actualizar y Eliminar) de libros para mantener una biblioteca digital organizada.  
- Autenticación y gestión de usuarios, permitiendo el inicio y cierre de sesión de manera segura.  
- Interfaz de usuario intuitiva que ofrece una experiencia fluida y moderna.  

Desarrollado utilizando el framework Django con énfasis en buenas prácticas, modularidad y diseño limpio.  

---  

## 🛠️ Requisitos del Sistema  
Para ejecutar esta aplicación necesitas:  
- Python 3.8 o superior.  
- Django 4.2 o superior.  
- pip para la gestión de dependencias.  
- Navegador web actualizado (Chrome, Firefox, Edge, etc.).  

---  

## 🚀 Instrucciones de Instalación  


### 1. Crear y Activar el Entorno Virtual  
Crea un entorno virtual para mantener aisladas las dependencias:  
```bash  
python -m venv venv  
```  

- **En Windows:**  
  ```bash  
  venv\Scripts\activate  
  ```  
- **En macOS/Linux:**  
  ```bash  
  source venv/bin/activate  
  ```  

### 2. Instalar las Dependencias  
Ejecuta el siguiente comando para instalar las dependencias listadas en el archivo `requirements.txt`:  
```bash  
pip install -r requirements.txt  
```  

### 3. Configurar la Base de Datos  
Aplica las migraciones para crear la estructura de la base de datos:  
```bash  
python manage.py makemigrations  
python manage.py migrate  
```  

---  

## 🖥️ Ejecución del Proyecto  
Inicia el servidor local con:  
```bash  
python manage.py runserver  
```  
Accede a la aplicación desde tu navegador en:  
```plaintext  
http://127.0.0.1:8000/  
```  

---  

## Funcionalidades Principales  

### 1. Inicio de Sesión 
Los usuarios pueden iniciar sesión de forma segura para acceder a las funcionalidades de la plataforma.  

### 2. Gestión de Libros 
Permite crear, editar, visualizar y eliminar libros desde una interfaz intuitiva.  

### 3. Registro de Usuarios
Facilita el registro de nuevos usuarios directamente desde la aplicación.  

---  

## 📋 Detalles Técnicos  

### Estructura del Proyecto  
El proyecto se organiza bajo la arquitectura estándar de Django:  
- **App `libros`:** Gestión completa de libros con operaciones CRUD.  
- Autenticación: Uso de las vistas predeterminadas de Django para login y logout, con personalización de las plantillas HTML.  

### Dependencias Clave  
- Django: Framework web principal.  
- SQLite: Base de datos por defecto, ideal para desarrollo y pruebas locales.  

---  

## 📧 Información de Contacto  

- Correo Electrónico: bsmatallanaj@itc.edu.co  
- GitHub: https://github.com/bsmatallanaj/PROGRAMACION_4
-  
