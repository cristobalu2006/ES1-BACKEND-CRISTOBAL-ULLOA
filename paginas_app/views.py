from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'index.html')

def mostrar_servicio(request):
    datos = [
        {
        "nombre": "lavado de vehículos",
        "valor": 10000
        },
        {
        "nombre": "Cambio de ruedas",
        "valor": 20000
        },
        {
        "nombre": "Cambio de color",
        "valor": 30000
        }
    ]
    return render(request, 'servicios.html', {'servicios':datos})