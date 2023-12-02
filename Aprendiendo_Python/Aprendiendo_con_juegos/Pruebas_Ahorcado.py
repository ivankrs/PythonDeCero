import tkinter as tk
from tkinter import ttk, messagebox, Label

def boton_a_presionado():
    'messagebox.showinfo(message= "Pruebas:   A", title= "Letra")'
    display_palabra.
    
def boton_b_presionado():
    messagebox.showinfo(message= "Pruebas:   B", title= "Letra")

def boton_c_presionado():
    messagebox.showinfo(message= "Pruebas:   C", title= "Letra")

def boton_d_presionado():
    messagebox.showinfo(message= "Pruebas:   D", title= "Letra")

def boton_e_presionado():
    messagebox.showinfo(message= "Pruebas:   E", title= "Letra")
    
def boton_f_presionado():
    messagebox.showinfo(message= "Pruebas:   F", title= "Letra")
    
def boton_g_presionado():
    messagebox.showinfo(message= "Pruebas:   G", title= "Letra")

def boton_h_presionado():
    messagebox.showinfo(message= "Pruebas:   H", title= "Letra")

def boton_i_presionado():
    messagebox.showinfo(message= "Pruebas:   I", title= "Letra")

def boton_j_presionado():
    messagebox.showinfo(message= "Pruebas:   J", title= "Letra")

def boton_k_presionado():
    messagebox.showinfo(message= "Pruebas:   K", title= "Letra")
    
def boton_l_presionado():
    messagebox.showinfo(message= "Pruebas:   L", title= "Letra")

def boton_m_presionado():
    messagebox.showinfo(message= "Pruebas:   M", title= "Letra")

def boton_n_presionado():
    messagebox.showinfo(message= "Pruebas:   N", title= "Letra")

def boton_ñ_presionado():
    messagebox.showinfo(message= "Pruebas:   Ñ", title= "Letra")

def boton_o_presionado():
    messagebox.showinfo(message= "Pruebas:   O", title= "Letra")
    
def boton_p_presionado():
    messagebox.showinfo(message= "Pruebas:   P", title= "Letra")

def boton_q_presionado():
    messagebox.showinfo(message= "Pruebas:   Q", title= "Letra")

def boton_r_presionado():
    messagebox.showinfo(message= "Pruebas:   R", title= "Letra")

def boton_s_presionado():
    messagebox.showinfo(message= "Pruebas:   S", title= "Letra")

def boton_t_presionado():
    messagebox.showinfo(message= "Pruebas:   T", title= "Letra")
    
def boton_u_presionado():
    messagebox.showinfo(message= "Pruebas:   U", title= "Letra")

def boton_v_presionado():
    messagebox.showinfo(message= "Pruebas:   V", title= "Letra")

def boton_w_presionado():
    messagebox.showinfo(message= "Pruebas:   W", title= "Letra")

def boton_x_presionado():
    messagebox.showinfo(message= "Pruebas:   X", title= "Letra")

def boton_y_presionado():
    messagebox.showinfo(message= "Pruebas:   Y", title= "Letra")
    
def boton_z_presionado():
    messagebox.showinfo(message= "Pruebas:   Z", title= "Letra")

#################################################################
 
def boton_a(event):
    boton_a_presionado()
    
def boton_b(event):
    boton_b_presionado()
    
def boton_c(event):
    boton_c_presionado()
    
def boton_d(event):
    boton_d_presionado()
    
def boton_e(event):
    boton_e_presionado()  

def boton_f(event):
    boton_f_presionado()
    
def boton_g(event):
    boton_g_presionado()
    
def boton_h(event):
    boton_h_presionado()
    
def boton_i(event):
    boton_i_presionado()
    
def boton_j(event):
    boton_j_presionado() 

def boton_k(event):
    boton_k_presionado()
    
def boton_l(event):
    boton_l_presionado()
    
def boton_m(event):
    boton_m_presionado()
    
def boton_n(event):
    boton_n_presionado()
    
def boton_ñ(event):
    boton_ñ_presionado() 

def boton_o(event):
    boton_o_presionado()
    
def boton_p(event):
    boton_p_presionado()
    
def boton_q(event):
    boton_q_presionado()
    
def boton_r(event):
    boton_r_presionado()
    
def boton_s(event):
    boton_s_presionado() 
    
def boton_t(event):
    boton_t_presionado()
    
def boton_u(event):
    boton_u_presionado()
    
def boton_v(event):
    boton_v_presionado()
    
def boton_w(event):
    boton_w_presionado()
    
def boton_x(event):
    boton_x_presionado() 

def boton_y(event):
    boton_y_presionado()
    
def boton_z(event):
    boton_z_presionado()
##########################################################

    
root = tk.Tk()

root.title("♦ El Ahorcado ♦")
root.config(width= 800, height= 500)

caja_de_pruebas = tk.Label(text = "♦ El  Ahorcado ♦", font = ("Times",25))
caja_de_pruebas.place(x = 305, y = 40)


palabra = '_ _ _ _ _ _'
display_palabra = tk.Label(text = palabra, font = ("Arial",25))
display_palabra.place(x = 130, y = 300)

display_tipo = tk.Label(text = "♦Un animal de 7 letras", font = ("Arial",15))
display_tipo.place(x = 40, y = 180)



boton_letra_a = tk.Button(text = "A",font=("Arial", 18) , command = boton_a_presionado)
boton_letra_a.bind("a", boton_a)
boton_letra_a.place(x = 45, y = 390, height=25 , width= 60)

boton_letra_b = tk.Button(text = "B", font=("Arial", 18) ,command = boton_b_presionado)
boton_letra_b.bind("b", boton_b)
boton_letra_b.place(x = 125, y = 390, height=25 , width= 60)

boton_letra_c = tk.Button(text = "C", font=("Arial", 18) ,command = boton_c_presionado)
boton_letra_c.bind("c", boton_c)
boton_letra_c.place(x = 205, y = 390, height=25 , width= 60)

boton_letra_d = tk.Button(text = "D", font=("Arial", 18) ,command = boton_d_presionado)
boton_letra_d.bind("d", boton_d)
boton_letra_d.place(x = 285, y = 390, height=25 , width= 60)

boton_letra_e = tk.Button(text = "E", font=("Arial", 18) ,command = boton_e_presionado)
boton_letra_e.bind("e", boton_e)
boton_letra_e.place(x = 365, y = 390, height=25 , width= 60)

boton_letra_e = tk.Button(text = "F", font=("Arial", 18) ,command = boton_f_presionado)
boton_letra_e.bind("f", boton_f)
boton_letra_e.place(x = 445, y = 390, height=25 , width= 60)

boton_letra_e = tk.Button(text = "G", font=("Arial", 18) ,command = boton_g_presionado)
boton_letra_e.bind("g", boton_g)
boton_letra_e.place(x = 525, y = 390, height=25 , width= 60)

boton_letra_e = tk.Button(text = "H", font=("Arial", 18) ,command = boton_h_presionado)
boton_letra_e.bind("h", boton_h)
boton_letra_e.place(x = 605, y = 390, height=25 , width= 60)

boton_letra_e = tk.Button(text = "I", font=("Arial", 18) ,command = boton_i_presionado)
boton_letra_e.bind("i", boton_i)
boton_letra_e.place(x = 685, y = 390, height=25 , width= 60)

boton_letra_e = tk.Button(text = "J", font=("Arial", 18) ,command = boton_j_presionado)
boton_letra_e.bind("j", boton_j)
boton_letra_e.place(x = 45, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "K", font=("Arial", 18) ,command = boton_k_presionado)
boton_letra_e.bind("k", boton_k)
boton_letra_e.place(x = 125, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "L", font=("Arial", 18) ,command = boton_l_presionado)
boton_letra_e.bind("l", boton_l)
boton_letra_e.place(x = 205, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "M", font=("Arial", 18) ,command = boton_m_presionado)
boton_letra_e.bind("m", boton_m)
boton_letra_e.place(x = 285, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "N", font=("Arial", 18) ,command = boton_n_presionado)
boton_letra_e.bind("n", boton_n)
boton_letra_e.place(x = 365, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "Ñ", font=("Arial", 18) ,command = boton_ñ_presionado)
boton_letra_e.bind("ñ", boton_ñ)
boton_letra_e.place(x = 445, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "O", font=("Arial", 18) ,command = boton_o_presionado)
boton_letra_e.bind("o", boton_o)
boton_letra_e.place(x = 525, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "P", font=("Arial", 18) ,command = boton_p_presionado)
boton_letra_e.bind("p", boton_p)
boton_letra_e.place(x = 605, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "Q", font=("Arial", 18) ,command = boton_q_presionado)
boton_letra_e.bind("q", boton_q)
boton_letra_e.place(x = 685, y = 425, height=25 , width= 60)

boton_letra_e = tk.Button(text = "R", font=("Arial", 18) ,command = boton_r_presionado)
boton_letra_e.bind("r", boton_t)
boton_letra_e.place(x = 45, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "S", font=("Arial", 18) ,command = boton_s_presionado)
boton_letra_e.bind("s", boton_s)
boton_letra_e.place(x = 125, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "T", font=("Arial", 18) ,command = boton_t_presionado)
boton_letra_e.bind("t", boton_t)
boton_letra_e.place(x = 205, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "U", font=("Arial", 18) ,command = boton_u_presionado)
boton_letra_e.bind("u", boton_u)
boton_letra_e.place(x = 285, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "V", font=("Arial", 18) ,command = boton_v_presionado)
boton_letra_e.bind("v", boton_v)
boton_letra_e.place(x = 365, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "W", font=("Arial", 18) ,command = boton_w_presionado)
boton_letra_e.bind("w", boton_w)
boton_letra_e.place(x = 445, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "X", font=("Arial", 18) ,command = boton_x_presionado)
boton_letra_e.bind("x", boton_x)
boton_letra_e.place(x = 525, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "Y", font=("Arial", 18) ,command = boton_y_presionado)
boton_letra_e.bind("y", boton_y)
boton_letra_e.place(x = 605, y = 460, height=25 , width= 60)

boton_letra_e = tk.Button(text = "Z", font=("Arial", 18) ,command = boton_z_presionado)
boton_letra_e.bind("z", boton_z)
boton_letra_e.place(x = 685, y = 460, height=25 , width= 60)













root.mainloop()