# Guess the number game.
import random

intentos = 0


print("\t-¡Hola! ¿Cúal es su nombre?")
player = input("-->")

numero = random.randint(1,20)
print("\t-Bueno, " + player + " estoy pensando en un numero del 1 al 20." )

for intentos in range(6): 
    print("\n\t-Intente adivinarlo.")
    guess = int(input("-->"))
    
    if guess < numero:
        print("\t\t-Tu número es muy bajo.")
        
    if guess > numero:
        print("\t\t-Tu número es muy alto.")
        
    if guess == numero:
        break

if guess == numero:
    intentos = str(intentos + 1)
    print("\t-¡Buen trabajo, " + player + "! ¡Adivinaste mi número en " + intentos + " intentos!" )
else:
    numero = str(numero)
    print("\t-Nop. El número que estába pensando era " + numero + ".")
    