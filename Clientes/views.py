#from django.http import HttpResponse
from django.shortcuts import render

datos_clientes = [
    {
        'Nombre': 'Nicolas',
        'Rut': '15.456.753-8',
        'Telefono': '9 5236 8741',
        'Email': 'nico@example.com',
        'Direccion': 'Estado 336',
        'Genero': 'Masculino' 
    }, 
    
    {
        'Nombre': 'Joaquin',
        'Rut': '18.258.963-8',
        'Telefono': '9 4125 6987',
        'Email': 'joaquin@example.com',
        'Direccion': 'Maipu 21',
        'Genero': 'Masculino' 
    }, 
    
    {
        'Nombre': 'Adolfo',
        'Rut': '15.456.753-8',
        'Telefono': '9 5236 8741',
        'Email': 'adolfo@example.com',
        'Direccion': 'Holanda 336',
        'Genero': 'Masculino' 
    }, 
    
    {
        'Nombre': 'Hans',
        'Rut': '17.365.147-8',
        'Telefono': '9 1236 8752',
        'Email': 'hans@example.com',
        'Direccion': 'Brasil 555',
        'Genero': 'Masculino' 
    }, 
    
    {
        'Nombre': 'Sofía',
        'Rut': '20.125.856-7',
        'Telefono': '9 6547 2547',
        'Email': 'sofia@example.com',
        'Direccion': 'Baquedano 336',
        'Genero': 'Femenino' 
    },
    {
        'Nombre': 'Barbara',
        'Rut': '25.125.789-7',
        'Telefono': '9 1254 7896',
        'Email': 'Barbara@example.com',
        'Direccion': 'Prat 224',
        'Genero': 'Femenino' 
    }
]

def clientes(request):
    contexto = {'clientesLlave': datos_clientes}
    return render(request, 'Clientes/clientes.html', contexto)
