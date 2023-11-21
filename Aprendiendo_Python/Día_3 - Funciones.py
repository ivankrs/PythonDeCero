# Pide ingresar un 'int'. Mensaje alterable
def get_int(mensaje = "Ingrese un número entero: "):
    numero_int = int(input(mensaje))
    return numero_int

# Pideingresar un 'float'. Mensaje alterable
def get_float(mensaje = "Ingrese un número: "):
    numero_float = float(input(mensaje))
    return numero_float

# Pide ingresar un nombre y capitaliza la primera letra. Mensaje alterable
def get_name(mensaje = "Ingrese su nombre: "):
    #print(mensaje)
    name = input(mensaje)
    
    return name.title()

# Pide ingresar un apellido y capitaliza la primera letra. Mensaje alterable
def get_surname(mensaje = "Ingrese su apellido: "):
    #print(mensaje)
    surname = input(mensaje)
    
    return surname.title()


número_1 = get_int(mensaje = 'Ingrese su edad: ')
número_2 = get_float(mensaje = 'Ingrese su salario: ')
nombre = get_name()
apellido = get_surname()
print("hola,", nombre, apellido, "de", número_1, "años", "con salario de", número_2)
 
