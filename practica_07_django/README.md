# Python-UTN

Ejercicio práctico-07 sobre la asignatura "Soporte a la Gestión de Datos con Programación Visual" resuelto con Django y SQLite3

### Creacion de un proyecto Django

- El comando para ejecutar el servidor de desarrollo es el siguiente: python manage.py runserver

El comando para crear un proyecto Django es el siguiente:

```
python -m django-admin startproject myproject
python -m django-admin startapp myproject .

python manage.py migrate            // Para hacer la migracion inicial del proyecto
python manage.py makemigrations     // Para crear el modelo
python manage.py createsuperuser    // Para crear un usuario administrador del proyecto (opcional)
```

### Comentarios aparte al ejecutar el servidor de desarrollo

- Al escribir la dirección http://127.0.0.1:8000/admin en el navegador, se puede acceder al panel de administración de Django. Para ello, se debe haber creado un usuario administrador con el comando `python manage.py createsuperuser` y haber iniciado sesión con él.
- Se puede agregar un nuevo usuario desde el panel de administración de Django, pero no se puede agregar un nuevo usuario desde la aplicación web. Esto se debe a que el modelo de usuario de Django no se puede modificar. Para poder agregar un nuevo usuario desde la aplicación web, se debe crear un nuevo modelo de usuario.
- Si hemos creado una tabla (en este caso "Socios") y queremos agregar un nuevo socio, podemos hacerlo desde el panel de administración de Django.
- {% csrf_token %} es un token de seguridad que se utiliza para proteger el formulario contra ataques de falsificación de solicitudes cruzadas (CSRF).
- {% loadstatic %} es un tag de plantilla que se utiliza para cargar archivos estáticos.
- Video de referencia: https://www.youtube.com/watch?v=uSbDMs7Y9yI
