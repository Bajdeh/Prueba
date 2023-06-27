import numpy
lista_rut=[]
lista_mascota=[]
numpy.zeros((2,5))
dias = 0
total = 0
def validar_rut():
            while True:
                
                    rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
                    if rut >= 1000000 and rut <= 99999999:
                        print("Su rut fue guardado con exito!")
                        return rut
                    else:
                        print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
                
def validar_nombreduenio():
     while True:
        duenio = input("Ingrese nombre del dueño: ")
        if len(duenio.strip()) >= 3 and duenio.isalpha():
            print("Su nombre fue guardado con exito!")
            return duenio
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombremascota():

    while True:
        nombre = input("Ingrese nombre de su mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            print("El nombre de su mascota fue guardado con exito!")
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_dias():
     
     while True:
        
            cantidad = int(input("Ingrese cantidad de dias:"))
            if cantidad >= 1:
                cantidad = cantidad + dias
                return cantidad
            else:
                print("ERROR! LA CANTIDAD DEBE ESTAR ENTRE 1 Y 6!")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                break
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def grabar():
    while True:
        validar_rut()
        validar_nombreduenio()

        validar_nombremascota()
        validar_dias()
        break

    hab=int(input("Ingrese Habitacion a seleccionar(1-10): "))

def buscar():
    rut=int(input("Ingrese rut a buscar: "))
    for rut in len(lista_rut):
            if rut in len(lista_rut):
                rut = x
    for x in len(lista_mascota):
        if x in len(lista_mascota):
              print("Su mascota si está")
        else:
             print("Su mascota no está :(")
              
def pagar():
     total = dias*15000
     print(f"su monto total a pagar es {total}")


def salir():
    if total== 0:
          print("Gracias por visitar :")
    else:
         print("tiene una deuda pendiente :")