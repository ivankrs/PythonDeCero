'''
La compania Rappi solicita un sistema que determine los días de vacaciones a los que tiene 
    derecho un trabajador.
Existen tres departamentos dentro de la compania con sus respectivas claves:
    1. Departamento de atención al cliente (clave 1)
    2. Departamento de logística (clave 2)
    3. Gerencia (clave 3)
    
Trabajador clave 1 (Atención al cliente):
    Con 1 año de servicio, reciben 6 días de vacaciones
    Con 2 a 6 año de servicio, reciben 14 días de vacaciones
    A partir de 7 año de servicio, reciben 20 días de vacaciones
    
Trabajador clave 2 (Logística):
    Con 1 año de servicio, reciben 7 días de vacaciones
    Con 2 a 6 año de servicio, reciben 15 días de vacaciones
    A partir de 7 año de servicio, reciben 22 días de vacaciones

Trabajador clave 3 (Gerencia):
    Con 1 año de servicio, reciben 10 días de vacaciones
    Con 2 a 6 año de servicio, reciben 20 días de vacaciones
    A partir de 7 año de servicio, reciben 30 días de vacaciones
    
Requerimientos indispensables:

El sistema debe de solicitar el "Nombre", "Clave de departamento" y "Atigüedad" del
    trabajador desde el teclado.
Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga el nombre del 
    trabajador y los dias de vacaciones a los que tenga derecho.

'''

import os, time

borrar_pantalla = lambda: os.system('cls')


borrar_pantalla()

def display(nombre='', apellido='',clave='', antigüedad=''):
    if clave == '1':
        clave = "Atención al cliente"
    if clave == '2':
        clave = "Logística" 
    if clave == '3':
        clave = "Gerencia"
    print(f'''
                        Plantilla   de    Vacaciones
                                   Rappi
    
    
    Nombre: {nombre} {apellido}
    Departamento: {clave}
    Antigüedad: {antigüedad}
          ''')
def is_char(cadena):
    for i in range(len(cadena)):
        if cadena[i] not in "abcdefghijklmnñopqrstuvwxyz ":
            return False
    if len(cadena) <= 2:
        return False
    return True

def get_name(mensaje = "Ingrese su nombre: ",\
            mensaje_reintento = "¡Solo se permiten 2 o más letras!"):
    
    while True:
        borrar_pantalla()
        display()
        name = input(mensaje).lower()
        if is_char(name):
            return name.title()
        else:
            print()
            print('\t\t',mensaje_reintento)
            time.sleep(2)
            

def get_surname(nombre, mensaje = "Ingrese su apellido: ",\
                mensaje_reintento = "¡Solo se permiten 2 o más letras!"):
  
    while True:
        borrar_pantalla()
        display(nombre)
        surname = input(mensaje).lower()
        if is_char(surname):
            return surname.title()
        else:
            print()
            print('\t\t',mensaje_reintento)
            time.sleep(2)
            
            
      
def is_int(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
    
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
            
def get_departamento_clave(nombre, apellido):
    while True:
        borrar_pantalla()
        display(nombre, apellido)
        clave = get_int(mensaje = '''Ingrese la calve de su departamento:
    1. Departamento de Atención al cliente (clave 1)
    2. Departamento de Logística (clave 2)
    3. Gerencia (clave 3)
    Numero ingresado: ''')
        if str(clave) not in "123":
            print("\n\tClave no valida, debe estar entre el 1 y 3")
            time.sleep(2)
            borrar_pantalla()
            continue
            
        else:
            return clave

def get_antigüedad(nombre, apellido,clave):
    while True:
        borrar_pantalla()
        display(nombre, apellido, clave)
        antigüedad = get_int(mensaje = "Ingrese su antigüedad en la empresa: ")
        if antigüedad > 51 or antigüedad < 1:
            print("\n\tLa antigüedad debe ser más de 0 y menos de 51 años")
            time.sleep(2)
            continue
        else:
            return antigüedad

def vacaciones_empleado(clave, antigüedad):
    clave = int(clave)
    antigüedad = int(antigüedad) 
    if antigüedad < 2:
        if clave == 1:
            vacaciones = 6
            return vacaciones
        if clave == 2:
            vacaciones = 7
            return vacaciones
        if clave == 3:
            vacaciones = 10
            return vacaciones
        
    elif antigüedad > 1 and antigüedad < 7:
        if clave == 1:
            vacaciones = 14
            return vacaciones
        if clave == 2:
            vacaciones = 15
            return vacaciones
        if clave == 3:
            vacaciones = 20
            return vacaciones
    else:
        if clave == 1:
            vacaciones = 20
            return vacaciones
        if clave == 2:
            vacaciones = 22
            return vacaciones
        if clave == 3:
            vacaciones = 30
            return vacaciones   
               
################################################################   >MAIN<
while True:
    borrar_pantalla()
    display()
    nombre = get_name()
    apellido = get_surname(nombre)
    clave = str(get_departamento_clave(nombre, apellido))
    antigüedad = str(get_antigüedad(nombre, apellido,clave))
    vacaciones = vacaciones_empleado(clave, antigüedad)
    if int(antigüedad) < 2:
        antigüedad += ' año'
    else:
        antigüedad += ' años'
    borrar_pantalla()
    display(nombre, apellido,clave, antigüedad)
    
    time.sleep(2)
    
    print(f">Le corresponde {vacaciones} días de vacaciones\n\n")
    time.sleep(1)
    input("\n...Presiona ENTER para continuar\n\n")
    
    borrar_pantalla()
    time.sleep(2)
    print("\n¿Qúiere ingresar otro empleado? (si / no)")
    if not input("\t>").lower().startswith('s'):
        print('\n'*3)
        break

    
    