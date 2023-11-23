import random
import time

def display_intro():
    print("Estas en una tierra llena de dragones. Frente a ti, se pueden ver dos cuevas. En una, se encuentra un dragon amigable que compartira su tesoro contigo. Y, en la otra, un dragon codisioso y hambriento, que te comera al verte.")
    print()
    
def choose_cave():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print("-->¿A cúal cueva ingresara?")
        cueva = input("-->")
        cueva = cueva
    return cueva

def check_cave(cueva):
    print("-Te acercas a la cueva...")
    time.sleep(2)
    print("-Esta oscuro y tenebroso...")
    time.sleep(2)
    print("-¡Un gran dragon salta en frente tuyo! Abre la boca y...")
    print()
    time.sleep(2)
    cueva_segura = random.randint(1,2)
    if cueva == str(cueva_segura):
        print("-¡Te dio parte de su tesoro!")
    else:
        print("-¡Te comio en un mordizco!")
        

play_again = "yes"
while play_again == "yes" or play_again == "y":
    display_intro()
    numero_cueva = choose_cave()
    check_cave(numero_cueva)
    play_again = input("¿Quiere juegar de nuevo? (yes or no)")