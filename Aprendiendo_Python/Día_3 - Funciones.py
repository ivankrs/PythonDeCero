# Valida que sea int
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
def get_int(mensaje = "Ingrese un número entero: "):
    
    while True:
        numero_int = input(mensaje)
        if is_int(numero_int):
            numero_int = int(numero_int)
            return numero_int
        else:
            print("Debe ingresar un número")
            continue
       

# Pideingresar un 'float'. Mensaje alterable
def get_float(mensaje = "Ingrese un número: "):
    while True:
        numero_float = input(mensaje)
        if is_float(numero_float):
            numero_float = float(numero_float)
            return numero_float
        else:
            print("Debe ingresar un número")
            continue
    
    return numero_float

# Pide ingresar un nombre y capitaliza la primera letra. Mensajes alterable
def get_name(mensaje = "Ingrese su nombre: ", mensaje_reintento = "¡Debe ingresar un nombre!: "):
    #print(mensaje)
    name = input(mensaje)
    while name == '':
        name = input(mensaje_reintento)
    
    return name.title()

# Pide ingresar un apellido y capitaliza la primera letra. Mensaje alterable
def get_surname(mensaje = "Ingrese su apellido: ", mensaje_reintento = "¡Debe ingresar un apellido!: "):
    #print(mensaje)
    surname = input(mensaje)
    while surname == '':
        surname = input(mensaje_reintento)
    
    return surname.title()


nombre = get_name()
apellido = get_surname()
número_1 = get_int(mensaje = 'Ingrese su edad: ')
número_2 = get_float(mensaje = 'Ingrese su salario: ')

print("Hola,", nombre, apellido, "de", número_1, "años", "con salario de", número_2)
print(type(número_1))
print(type(número_2))
