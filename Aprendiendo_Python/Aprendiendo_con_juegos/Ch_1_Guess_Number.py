# Guess the number game.
import random

intentos = 0


print("¡Hola! ¿Cúal es su nombre?")
player = input()

numero = random.randint(1,20)
print("Bueno, " + player + " estoy pensando en un numero del 1 al 20." )

for intentos in range(6): 
    print("Intente adivinarlo.")
    guess = int(input())
    
    if guess < numero:
        print("Tu número es muy bajo.")
        
    if guess > numero:
        print("Tu número es muy alto.")
        
    if guess == numero:
        break

if guess == numero:
    intentos = str(intentos + 1)
    print("¡Buen trabajo, " + player + "! ¡Adivinaste mi número en " + intentos + " intentos!" )
else:
    numero = str(numero)
    print("Nop. El número que estába pensando era " + numero + ".")
    