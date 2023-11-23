import random


numero_1 = random.randint(1,10)
numero_2 = random.randint(1,10)

print("¿Cúal es la suma de " + str(numero_1)+ "+" + str(numero_2) + "?")

respuesta = int(input())

if respuesta == numero_1 + numero_2:
    print("¡Es correcto!")
else:
    print("¡Nop!. La respuesta es: " + str(numero_1 + numero_2))
