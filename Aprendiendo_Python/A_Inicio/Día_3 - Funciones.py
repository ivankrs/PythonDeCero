# Valida que sea int
import time, os

borrar_pantalla = lambda: os.system("cls")

def is_int(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
# Valida que sea float
def is_float(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False    
# Pide ingresar un 'int'. Mensaje alterable
def get_int(mensaje = "Ingrese un número entero: ",\
            mensaje_reintento = "Solo se permiten números enteros"):
    
    while True:
        numero_int = input(mensaje)
        if is_int(numero_int):
            numero_int = int(numero_int)
            return numero_int
        else:
            print()
            print('\t\t',mensaje_reintento)
            time.sleep(1)
            print()
       

# Pideingresar un 'float'. Mensaje alterable
def get_float(mensaje = "Ingrese un número: ",\
            mensaje_reintento = "¡Solo se permiten números!"):
    
    while True:
        numero_float = input(mensaje)
        if is_float(numero_float):
            numero_float = float(numero_float)
            return numero_float
        else:
            print()
            print('\t\t',mensaje_reintento)
            time.sleep(1)
            print()

def is_char(cadena):
    for i in range(len(cadena)):
        if cadena[i] not in "abcdefghijklmnñopqrstuvwxyz":
            return False
    if len(cadena) < 2:
        return False
    return True
    
# Pide ingresar un nombre y capitaliza la primera letra. Mensajes alterable
def get_name(mensaje = "Ingrese su nombre: ",\
            mensaje_reintento = "¡Solo se permiten 2 o más letras!"):
    #print(mensaje)
    while True:
        name = input(mensaje).lower()
        if is_char(name):
            return name.title()
        else:
            print()
            print('\t\t',mensaje_reintento)
            time.sleep(1)
            print()

# Pide ingresar un apellido y capitaliza la primera letra. Mensaje alterable
def get_surname(mensaje = "Ingrese su apellido: ",\
                mensaje_reintento = "¡Solo se permiten 2 o más letras!"):
    #print(mensaje)  
    while True:
        surname = input(mensaje).lower()
        if is_char(surname):
            return surname.title()
        else:
            print()
            print('\t\t',mensaje_reintento)
            time.sleep(1)
            print()


nombre = get_name()
apellido = get_surname()
número_1 = get_int(mensaje = 'Ingrese su edad: ')
número_2 = get_float(mensaje = 'Ingrese su salario: ')

print("Hola,", nombre, apellido, "de", número_1, "años", "con salario de", número_2)
print(type(número_1))
print(type(número_2))
