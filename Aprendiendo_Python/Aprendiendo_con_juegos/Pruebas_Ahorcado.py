import tkinter as tk
from tkinter import ttk

def boton_a_presionado():
    caja_de_pruebas.config(text = "Pruebas:   A")

root = tk.Tk()

root.title("♦ El Ahorcado ♦")
root.config(width= 400, height= 300)

boton_letra_a = ttk.Button(text = "A", command = boton_a_presionado)
boton_letra_a.place(x = 20, y = 80)

caja_de_pruebas = ttk.Label(text = "Pruebas: n/a")
caja_de_pruebas.place(x = 20, y = 40)






root.mainloop()