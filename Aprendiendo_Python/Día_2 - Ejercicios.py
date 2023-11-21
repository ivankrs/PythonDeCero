'''
1.
Escribí un programa que solicite al usuario que ingrese su nombre.
El nombre se debe almacenar en una variable llamada nombre.
A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”,
donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.


# 'input()' recibe str. int(input())--> recibira 'int' ahora

nombreUsuario = input("¿Cúal es su nombre? ")
edadUsuario = int(input("¿Cúantos años tiene? "))

print("Su nombre se cargo en el sistema,", nombreUsuario)
print("Su edad se cargo en el sistema,", edadUsuario)
'''
'''
2.
Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable.
A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable.
En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario.
Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, 
donde “[suma]” se reemplazará por el resultado de la operación.


variableFloat = float(input("Ingrese un número decimal: "))
variableInt = int(input("Ingrese un número entero: "))
suma = variableFloat + variableInt

print("El resultado de la suma es", suma)
'''
'''
3.
Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable.
Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.


numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
suma = numero1 + numero2

print()
print("El resultado de la suma es", suma)

numero3 = float(input("Tercer número: "))
multiplicación = numero3 * suma

print()
print("El resultado de la multiplicación es", multiplicación)

'''
'''
4.
Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta 
y la cantidad de litros de combustible que consumió durante ese recorrido. 
Mostrar el consumo de combustible por kilómetro.


kilometroRecorre = float(input("Cantidad de kilometros recorridos: "))
litroConsumido = float(input("Litros de combustible consumido: "))

print("El consumo de combustible por kilometro es de", kilometroRecorre/litroConsumido)
'''
'''
5.
Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit 
(debe permitir decimales)y le muestre el equivalente en grados Celsius. 
La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_

fahrenheit = float(input("Ingrese una teperatura en F°: "))
celsius = (5/9) * (fahrenheit-32)

print("La temperatura en C° es:", celsius)
'''

'''
6.
Escribí un programa que solicite al usuario ingresar tres números 
para luego mostrarle el promedio de los tres.

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = (n1+n2+n3)/3
print("El promedio es:", promedio)
'''

'''
7.
Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. 
A continuación, mostrar el resultado final en pantalla.

n1 = float(input("Un número: "))

print("El resultado con 15% es:", n1-(n1*15/100))
'''

'''
8.
Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales 
se guardarán en dos variables distintas. 
A continuación, almacená en una variable la concatenación de la primera palabra, 
más un espacio, más la segunda palabra.
Mostrá este resultado en pantalla


p1 = input("Primera palabra: ")
p2 = input("Segunda palabra: ")
frase = p1 +" "+ p2

print(p1+" "+p2)
print()
print(frase)
'''

'''
9.
Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable.
A continuación, mostrar en pantalla la primera letra del texto ingresado. 
Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que 
tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4)
y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.


frase = input("Ingrese texto: ")
print("La primera letra del texto es:", frase[0])
print("Ingrese un número positivo menor a:", len(frase))
i = int(input())
print("La letra del texto en funcion al indice es:", frase[i])
print(frase)
'''
'''
10.
Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año
y almacene ese número en una variable.
A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario 
ha visto más de 3 shows.
'''

shows = int(input("Cantidad de shows vistos: "))
print(shows > 3)