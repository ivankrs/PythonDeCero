import random
import time

print("Voy a lanzar una moneda 1000 veces. ¿Puedes adivinar cuantas veces sera cara? (Presione ENTER para iniciar)")
input()
print("Okey. Iniciare las lanzadas de monedas")
time.sleep(2)
print("\n"*2)

flips = 0
caras = 0

while flips < 1000:
    if random.randint(0,1) == 1:
        caras = caras + 1
    flips = flips +1
    
    if flips == 100:
        print("Vamos por las primeras 100 y caras an salido " + str(caras) + " veces.")
        print("\n"*2)
        time.sleep(1)
        
    if flips == 500:
        print("Ya vamos por la mitad y caras an salido " + str(caras) + " veces.")
        print("\n"*2)
        time.sleep(2)

    if flips == 900:
        print("Ya vamos terminando y caras an salido " + str(caras) + " veces.")
        print("\n"*2)
        time.sleep(3)
print("De las 1000 lanzadas, caras an salido " + str(caras) + " veces.")
print("¿Estuvo cerca del número que elejiste?")

