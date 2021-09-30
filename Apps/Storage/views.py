from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        nombre = request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        telefono=request.POST.get('telefono')
        direccion=request.POST.get('direccion')
        nombremasc=request.POST.get('nombremasc')
        raza=request.POST.get('raza')
        edad=request.POST.get('edad')

        print(nombre + ' ' + apellido)
        print(telefono + ' ' + direccion)
        print(nombremasc + ' ' + raza)
        print(edad)

        model_empleado = cliente(nombre=nombre,
                                  apellido=apellido,
                                  telefono=telefono,
                                  direccion=direccion)

        model_mascota=mascota(nombremasc=nombremasc,
                               raza=raza,
                               edad=edad)

        model_empleado.save()
        model_mascota.save()
        return redirect('Storage:index')

    elif request.method == 'GET':
        return render(request, 'index.html')

