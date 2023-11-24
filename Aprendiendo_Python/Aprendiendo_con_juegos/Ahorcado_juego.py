import random
import time
import os
DECORATIO_PICS = ['''

░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
░░░░░░░░░░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░█░░░█░░░░░░░░░░░░░
░░░░░░░░░█░░░░█░░░░░░░░░░░░░
██████▄▄█░░░░░██████▄░░░░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░
▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░
█████▀░░░░▀▀████████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░
╔════╗░░╔════╗╔═══╗░░░░░░░░░
║████║░░║████║║███╠═══╦═════╗
╚╗██╔╝░░╚╗██╔╩╣██╠╝███║█████║
░║██║░░░░║██║╔╝██║███╔╣██══╦╝
░║██║╔══╗║██║║██████═╣║████║
╔╝██╚╝██╠╝██╚╬═██║███╚╣██══╩╗
║███████║████║████║███║█████ ''']
HANGMAN_PICS = ['''
                +---+
                    ¦
                    ¦
                    ¦
                   ===''','''
                +---+
                O   ¦
                    ¦
                    ¦
                   ===''','''
                +---+
                O   ¦
                ¦   ¦
                    ¦
                   ===''','''
                +---+
                O   ¦
               /¦   ¦
                    ¦
                   ===''','''
                +---+
                O   ¦
               /¦\  ¦
                    ¦
                   ===''','''
                +---+
                O   ¦
               /¦\  ¦
               /    ¦
                   ===''','''
                +---+
                O   ¦
               /¦\  ¦
               / \  ¦
                   ===''','''
                +---+
               *O*  ¦
               /¦\  ¦
               / \  ¦
                   ===''','''
                +---+
               *O*  ¦
               /¦\  ¦
              _/ \_ ¦
                   ===''']

lista_de_animales = ['Aguila', 'Avestruz', 'Ballena', 'Bisonte', 'Bufalo', 'Buho', 'Buitre', 'Burro', 'Caballo',
                    "Cabra", "Camaleón", "Camello", "Canario", "Castor", "Cebra", "Cerdo", "Chancho", "Ciervo", "Cobra", "Colibrí" ,"Comadreja",
                    "Cóndor" ,"Conejo" ,"Delfín","Elefante", "Faisan" ,"Flamenco" ,"Foca" ,"Gallina" ,"Gallo" ,"Gato" ,"Gorila", "Guepardo",
                    "Hámster", "Hiena", "Hipopótamo", "Jabalí" ,"Jaguar", "Jirafa" ,"Koala" ,"Lagarto" ,"León" ,"León marino", "Llama", "Lobo",
                    "Loro", "Manatís", "Mapache", "Mono", "Murciélago", "Nutria", "Ñandú", "Orca" ,"Oso hormiguero" ,"Oso", "Oso polar",
                    "Pájaro carpintero", "Paloma", "Panda", "Pato", "Pavo real", "Pelícano",  "Pingüino", "Puercoespín", "Puma",
                    "Rana", "Ratón", "Reno", "Rinoceronte", "Salamandra", "Sapo", "Serpiente", "Tapir", "Tejon", "Tiburón", "Tigre",
                    "Topo","Toro", "Tucán" ,"Vaca" ,"Vicuña", "Zorrillo", "Zorro"]

lista_de_figuras_geometricas = ["triángulo", "rectángulo", "cuadrado", "trapecio", "hexágono", "rombo", "círculo", "pentágono", "octógono", "poligono"]

lista_de_frutas = ["melón", "naranja", "ananá", "ciruela", "cereza", "durazno", "frambuesa", "mora", "manzana", "sandía", "uva", "limón", "pera", "arándanos", "frutilla", "mandarina", "banana"]

lista_de_verduras = ["zanahoria", "zapallo", "calabaza", "Aceitunas", "acelga", "apio", "batata", "papa", "radicheta", "remolacha", "repollo", "espinaca", "lechuga", "cebolla", "choclo", "brocoli"]

lista_de_colores = ["Negro", "azul", "marrón", "gris", "verde", "naranja", "rosa", "violeta", "rojo", "blanco", "amarillo"]
directorio_de_listas =[lista_de_figuras_geometricas, lista_de_animales, lista_de_colores, lista_de_frutas, lista_de_verduras]
borrarPantalla = lambda: os.system ("cls")
# Reemplaza la vocal con tilde por la misma sin tilde.
def replace_vocals(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def obtener_lista_aleatoria(directorio_de_listas):
    lista_aleatoria = random.choice(directorio_de_listas)
    return lista_aleatoria

def obtener_palabra_aleatoria(lista_palabras):
    palabra_aleatoria = random.choice(lista_palabras)
    return palabra_aleatoria

def obtener_letra(letras_adivinadas,letras_erradas,palabra_secreta,lista):
    letras_intentadas = letras_adivinadas + letras_erradas
            
    while len(HANGMAN_PICS)>len(letras_erradas):
        letra = input("->Ingrese una letra.\n--->").lower()
        
        if len(letra) != 1:
            borrarPantalla()
            display(palabra_secreta, letras_adivinadas, letras_erradas, HANGMAN_PICS,lista)
            time.sleep(1)
            print("\n>>Por favor igrese solo 'una' letra.\n")
            time.sleep(1)
            
        elif letra in letras_intentadas:
            borrarPantalla()
            display(palabra_secreta, letras_adivinadas, letras_erradas, HANGMAN_PICS,lista)
            time.sleep(1)
            print("\n>>Ya habias elejido esa letra. Elija de nuevo.\n")
            time.sleep(1)
            
        elif letra not in "abcdefghijklmnñopqrstuvwxyz":
            borrarPantalla()
            display(palabra_secreta, letras_adivinadas, letras_erradas, HANGMAN_PICS,lista)
            time.sleep(1)
            print("\n>>Por favor ingrese una LETRA.\n")
            time.sleep(1)
        else:
            return letra
            
            
      

def display(palabra_secreta, letras_adivinadas,letras_erradas, HANGMAN_PICS, lista):
    espacios = ''*len(palabra_secreta)
    letras_intentadas = letras_adivinadas + letras_erradas
    
    print("\tE L    A H O R C A D O\n" + HANGMAN_PICS[len(letras_erradas)])
      
    if lista == lista_de_animales:
        tipo = 'Animal'
    elif lista == lista_de_colores:
        tipo = 'Color'
    elif lista == lista_de_frutas:
        tipo = 'Fruta'
    elif lista == lista_de_verduras:
        tipo = 'Verdura'
    else:
        tipo = 'Figura geometrica'
    
    if ' ' in palabra:
        print("\t\t>",tipo,"de:" ,str(len(palabra)-1), "letras.\n")
    else:
        print("\t\t>",tipo,"de:" ,str(len(palabra)), "letras.\n")

    for i in range(len(palabra_secreta)):
        if ' ' in palabra_secreta:
            letras_adivinadas += ' '
                    
        if palabra_secreta[i] in letras_adivinadas:
            espacios = espacios[:i] + palabra_secreta[i].upper() + espacios[i+1:]
        else:
            espacios += '_'
    print(end = '')
    for letra in espacios:
        print(letra ,end = ' ')
        
    print("\n\nLetras intentadas: ", end = '')
    for letra in letras_intentadas:
        print(letra, end = '-')
    print()
  
def gano_el_juego(palabra, letras_correctas):
    palabra_con_tilde = palabra
    palabra = replace_vocals(palabra)
    
    if ' ' in palabra:
        letras_correctas += ' '
        
    if set(letras_correctas.lower()) == set(palabra.lower()):
            print("--------------------------\n")
            print(palabra_con_tilde)
            print("\n--------------------------\n")
            time.sleep(2)
            borrarPantalla()
            print("¡Felizidades, has ganado!")
            input("\nPresiona ENTER para continuar\n")
            print()
            return True
    else:
        return False

def perdio_el_juego(letras_erradas, HANGMAN_PICS, palabra):
    if len(letras_erradas) == len(HANGMAN_PICS):
        borrarPantalla()
        print("\n\n>>Se han acabado los intentos...")
        time.sleep(1)
        print("\n\n>La palabra era '" + palabra + "'.")
        input("\nPresiona ENTER para continuar\n")
        return True
    else:
        return False
    
def play_again():
    return input("¿Quieres volver a jugar? (si o no): ").lower().startswith('s')

#############################################
lista = obtener_lista_aleatoria(directorio_de_listas) 
palabra_con_tilde = obtener_palabra_aleatoria(lista).upper()
palabra = replace_vocals(palabra_con_tilde).lower()
letras_erradas = ''
letras_correctas = ''
letras_intentadas = ''
fin_del_juego = False

##############################################


while True:
    borrarPantalla()
    display(palabra, letras_correctas, letras_erradas,HANGMAN_PICS, lista)
    
    print()
        
    intento = obtener_letra(letras_correctas, letras_erradas,palabra,lista)
    
    if intento in palabra:
        letras_correctas += intento
        
        fin_del_juego = gano_el_juego(palabra_con_tilde, letras_correctas)  
    else:
        letras_erradas += intento
        
        fin_del_juego = perdio_el_juego(letras_erradas,HANGMAN_PICS,palabra_con_tilde)
        
    #letras_intentadas = letras_erradas + letras_correctas    
    borrarPantalla()
    print()
    
    if fin_del_juego:
        time.sleep(1)
        if play_again():
            
            lista = obtener_lista_aleatoria(directorio_de_listas)
            palabra_con_tilde = obtener_palabra_aleatoria(lista).upper()
            palabra = replace_vocals(palabra_con_tilde).lower()
            letras_erradas = ''
            letras_correctas = ''
            letras_intentadas = ''
            fin_del_juego = False
            borrarPantalla()
            print()            
        else:
            borrarPantalla()
            print("\nGracias por jugar")
            time.sleep(2)
            borrarPantalla()
            print(DECORATIO_PICS[0])
            break
        
        
        
        
        
