# Día 1 Aprendiendo Python:


# El '#' se usa para comentarios de una linea

"""
Con comillas se puede hacer comentarios.
Se puede usar para comentarios de n lineas.
"""
'''
Con comillas simples tambien se puede comentar n lineas
'''
# No hace falta agregar el ';' al final

# Imprime Hola python; se puede usar comillas dobles o simples para los prints.

print("Hola python")
print('Hola python')

# La funcion 'type()' me dice el tipo de dato.

# tipo 'str' string.
print(type("Hola python"))

# tipo 'int' número entero.
print(type(5))

# tipo 'float' número flotante.
print(type(1.2))

# tipo 'bool' True o False.
print(type(True))

'''
No hace falta declarar variables, solo inicializarlas.
El condicional 'if' no usa corchetes, se usan los ':'.
'''
temperatura = 40

if temperatura > 35 :
    print("Aviso por alta temperatura")
    
else:
    
    if temperatura < 10 :
        print("Aviso por baja temperatura")
        
    else:
        print("Parámetros normales")

# Se puede acortar el codigo usando 'elif' en vez de un 'if' despues de un 'else'

if temperatura > 35 :
    print("Aviso por alta temperatura")
    
elif temperatura < 10 :
    print("Aviso por baja temperatura")
    
else:
    print("Parámetros normales")