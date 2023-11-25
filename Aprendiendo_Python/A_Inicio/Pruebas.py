'''import pygame, sys

from pygame.locals import *

 

pygame.init()
#crea ventana                       #ancho,largo
DISPLAYSURF = pygame.display.set_mode((800, 700))

pygame.display.set_caption('Juego el Ahorcado')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()'''

import tkinter as tk
from tkinter import ttk

def convertir_temp():
    temp_celsius = float(caja_temp_celcius.get())
    temp_kelvin = temp_celsius +273.15
    temp_fahrenheit = temp_celsius *1.8 +32
    
    etiqueta_temp_kelvins.config(text = f"Temperatura en K: {temp_kelvin}")
    etiqueta_temp_fahrenheit.config(text = f"Temperatura en F: {temp_fahrenheit}")

def archivo_nuevo_presionado():
    print("¡Has presionado para crear un nuevo archivo!")
    
    
root = tk.Tk()

root.title("Convertor de Temperatura")
root.config(width = 400, height= 300)

barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff = False)

menu_archivo.add_command(label = "Nuevo", accelerator = "Ctrl+N", command = archivo_nuevo_presionado)

barra_menus.add_cascade(menu = menu_archivo, label = "Archivo")
root.config(menu = barra_menus)

etiqueta_temp_celcius = ttk.Label(text = "Temperatura en C°:")
etiqueta_temp_celcius.place(x = 20, y = 40)

caja_temp_celcius = ttk.Entry()
caja_temp_celcius.place(x = 140, y = 40, width= 60)

boton_convertir = ttk.Button(text="Convertir", command = convertir_temp)
boton_convertir.place(x = 20, y = 75)

etiqueta_temp_kelvins = ttk.Label(text = "Temperatura en K°: n/a")
etiqueta_temp_kelvins.place(x = 20, y = 120 )

etiqueta_temp_fahrenheit = ttk.Label(text = "Temperatura en F°: n/a")
etiqueta_temp_fahrenheit.place(x = 20, y = 160)

root.mainloop() #Debe quedar al final, todo por debajo no se mostrara