from django.shortcuts import render, redirect
from .models import Socio
from django.contrib import messages 

# Create your views here.

def home(request):
    sociosListados = Socio.objects.all()                        #? Trae todos los socios de la base de datos
    messages.success(request, 'Socios listados correctamente!')  #? Muestra un mensaje de exito

    return render(request, 'gestionSocios.html', {'socios': sociosListados})    #? Renderiza la vista gestionSocios.html y le pasa como parametro la lista de socios

def registrarSocio(request):
    dni = request.POST['txtdni']
    nombre = request.POST['txtnombre']
    apellido = request.POST['txtapellido']
    email = request.POST['txtemail']

    socio = Socio.objects.create(dni=dni, nombre=nombre, apellido=apellido, email=email)
    messages.success(request, 'Socio registrado correctamente!')
    return redirect('/')                                            #? Redirecciona a la pagina principal

def edicionSocio(request, dni):
    socio = Socio.objects.get(dni=dni)
    return render(request, 'editarSocio.html', {'socio': socio})

def editarSocio(request):
    dni = request.POST['txtdni']
    nombre = request.POST['txtnombre']
    apellido = request.POST['txtapellido']
    email = request.POST['txtemail']

    socio = Socio.objects.get(dni=dni)
    socio.nombre = nombre
    socio.apellido = apellido
    socio.email = email
    socio.save()

    messages.success(request, 'Socio editado correctamente!')
    return redirect('/')

def eliminarSocio(request, dni):
    socio = Socio.objects.get(dni=dni)
    socio.delete()
    messages.success(request, 'Socio eliminado correctamente!')
    return redirect('/')