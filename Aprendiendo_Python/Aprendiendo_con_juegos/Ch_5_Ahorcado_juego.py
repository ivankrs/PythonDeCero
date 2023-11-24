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
                   ===''']

lista_de_palabras = ['Aguila', 'Avestruz', 'Ballena', 'Bisonte', 'Bufalo', 'Buho', 'Buitre', 'Burro', 'Caballo',
                    "Cabra", "Camaleón", "Camello", "Canario", "Castor", "Cebra", "Cerdo", "Chancho", "Ciervo", "Cobra", "Colibrí" ,"Comadreja",
                    "Cóndor" ,"Conejo" ,"Delfín","Elefante", "Faisan" ,"Flamenco" ,"Foca" ,"Gallina" ,"Gallo" ,"Gato" ,"Gorila", "Guepardo",
                    "Hámster", "Hiena", "Hipopótamo", "Jabalí" ,"Jaguar", "Jirafa" ,"Koala" ,"Lagarto" ,"León" ,"León marino", "Llama", "Lobo",
                    "Loro", "Manatís", "Mapache", "Mono", "Murciélago", "Nutria", "Ñandú", "Orca" ,"Oso hormiguero" ,"Oso", "Oso polar",
                    "Pájaro carpintero", "Paloma", "Panda", "Pato", "Pavo real", "Pelícano",  "Pingüino", "Puercoespín", "Puma",
                    "Rana", "Ratón", "Reno", "Rinoceronte", "Salamandra", "Sapo", "Serpiente", "Tapir", "Tejon", "Tiburón", "Tigre",
                    "Topo","Toro", "Tucán" ,"Vaca" ,"Vicuña", "Zorrillo", "Zorro"]
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

def obtener_palabra_aleatoria(lista_palabras):
    palabra_aleatoria = random.choice(lista_palabras)
    return palabra_aleatoria

def obtener_letra(letras_intentadas,letras_erradas):
    while len(HANGMAN_PICS)>len(letras_erradas):
        letra = input("->Ingrese una letra.\n--->").lower()
        if len(letra) != 1:
                print("Por favor igrese solo 'una' letra.")
        elif letra in letras_intentadas:
            print("Ya habias elejido esa letra. Elija de nuevo.")
        elif letra not in "abcdefghijklmnñopqrstuvwxyz":
            print("Por favor ingrese una LETRA.")
        else:
            break
            
    return letra  

def palabra_con_espacios(palabra): #Si hay espacio 
    for i in range(len(palabra)):
        if palabra[i]==' ':
            return True
        else:
            break
    return False

def display(palabra_secreta, letras_adivinadas):
    espacios = ''*len(palabra_secreta)
        
    for i in range(len(palabra_secreta)):
        if ' ' in palabra_secreta:
            palabra_secreta = palabra_secreta.replace(" ", "-")
            letras_adivinadas += '-'
                    
        if palabra_secreta[i] in letras_adivinadas:
            espacios = espacios[:i] + palabra_secreta[i].upper() + espacios[i+1:]
        else:
            espacios += '_'
    print(end = '')
    for letra in espacios:
        print(letra, end = ' ')
  
def gano_el_juego(palabra, letras_correctas):
    palabra_con_tilde = palabra
    palabra = replace_vocals(palabra)
    
    if ' ' in palabra:
        palabra = palabra.replace(" ", "-")
        letras_correctas += '-'
        
    if set(letras_correctas.lower()) == set(palabra.lower()):
            print("--------------------------\n")
            print(palabra_con_tilde)
            print("\n--------------------------\n")
            time.sleep(2)
            print("¡Felizidades, has ganado!")
            input("\nPresiona ENTER para continuar\n")
            print()
            return True
    else:
        return False

def perdio_el_juego(letras_erradas, HANGMAN_PICS, palabra):
    if len(letras_erradas) == len(HANGMAN_PICS):
        print("Se han acabado los intentos...\n\nLa palabra era '" + palabra + "'.")
        input("\nPresiona ENTER para continuar\n")
        return True
    else:
        return False
    
def play_again():
    return input("¿Quieres volver a jugar? (si o no): ").lower().startswith('s')

############################################# 
palabra_con_tilde = lista_de_palabras[44].upper()#obtener_palabra_aleatoria(lista_de_palabras).upper()#lista_de_palabras[42].upper()
palabra = replace_vocals(palabra_con_tilde).lower()
letras_erradas = ''
letras_correctas = ''
letras_intentadas = ''
fin_del_juego = False
borrarPantalla = lambda: os.system ("cls")
##############################################


while True:
    print("\tE L    A H O R C A D O\n" + HANGMAN_PICS[len(letras_erradas)])
    print()
    display(palabra, letras_correctas)
    print()    
    print("Letras erradas: ", end = '')
    for letra in letras_erradas:
        print(letra, end = '-')
    print()
        
    intento = obtener_letra(letras_intentadas, letras_erradas)
    
    if intento in palabra:
        letras_correctas += intento
        letras_intentadas = letras_erradas + letras_correctas
        
        palabra_con_espacios(palabra)
        fin_del_juego = gano_el_juego(palabra_con_tilde, letras_correctas)  
    else:
        letras_erradas += intento
        fin_del_juego = perdio_el_juego(letras_erradas,HANGMAN_PICS,palabra_con_tilde)
        
    borrarPantalla()
    print()
    
    if fin_del_juego:
        time.sleep(1)
        if play_again():
            palabra_con_tilde = obtener_palabra_aleatoria(lista_de_palabras).upper()
            palabra = replace_vocals(palabra_con_tilde).lower()
            letras_erradas = ''
            letras_correctas = ''
            letras_intentadas = ''
            fin_del_juego = False
            print('\n'*3)
        else:
            print("\nGracias por jugar")
            time.sleep(2)
            borrarPantalla()
            print(DECORATIO_PICS[0])
            break
        
        
        
        
        
