import Funciones_prueba3

total = 0
lista_rut=[]
lista_nombre=[]
lista_mascota=[]
dias=0
import numpy
numpy.zeros((2,5))

while True:
    print("""
    1.Ingresar datos para agendar habitacion: 
    2.Busque a su mascota en el hotel: 
    3.Pagar el monto total:
    4.Salir
    """)

   
    Funciones_prueba3.validar_opcion()
    Funciones_prueba3.grabar()
    Funciones_prueba3.buscar()
    Funciones_prueba3.pagar()
    Funciones_prueba3.salir()




    
    if Funciones_prueba3.validar_opcion():
        Funciones_prueba3.grabar()
        
    elif Funciones_prueba3.validar_opcion():
        Funciones_prueba3.buscar()

    elif Funciones_prueba3.validar_opcion():
        Funciones_prueba3.pagar()

    else:
        Funciones_prueba3.salir()
        break
