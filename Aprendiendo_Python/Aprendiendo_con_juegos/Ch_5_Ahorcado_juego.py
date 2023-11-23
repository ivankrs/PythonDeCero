import random
import time
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
    palabra_aleatoria = random.choice(lista_palabras).lower()
    return palabra_aleatoria
    
def display(palabra_secreta, letras_adivinadas):
    espacios = ''*len(palabra_secreta)
    for i in range(len(palabra_secreta)):
        #for letra in palabra_secreta:
        if palabra_secreta[i] in letras_adivinadas:
                espacios = espacios[:i] + palabra_secreta[i].upper() + espacios[i+1:]
        else:
            espacios += '_'
    print(end = '')
    for letra in espacios:
        print(letra, end = ' ')

def play_again():
    return input("¿Quieres volver a jugar? (si o no): ").lower().startswith('s')


palabra = obtener_palabra_aleatoria(lista_de_palabras)
palabra = replace_vocals(palabra)    
letras_erradas = ''
letras_correctas = ''
letras_intentadas = ''
fin_del_juego = False
print(palabra)


while True:
    print("\tE L    A H O R C A D O\n" + HANGMAN_PICS[len(letras_erradas)])
    print()
    display(palabra, letras_correctas)
    print()    
    print("Letras erradas: ", end = '')
    for letra in letras_erradas:
        print(letra, end = '-')
    print()
        
    while True:
        intento = input("->Ingrese una letra.\n--->")
        intento = intento.lower()
        if len(intento) != 1:
            print("Por favor igrese solo 'una' letra.")
        elif intento in letras_intentadas:
            print("Ya habias elejido esa letra. Elija de nuevo.")
        elif intento not in "abcdefghijklmnñopqrstuvwxyz":
            print("Por favor ingrese una LETRA.")
        else:
            break
    
    if intento in palabra:
        letras_correctas += intento
        letras_intentadas = letras_erradas + letras_correctas
        
        if set(letras_correctas) == set(palabra.lower()):
            print('\n'*1)
            display(palabra, letras_correctas)
            print('\n'*1)
            time.sleep(2)
            print("¡Felizidades, has ganado!")
            print()
            fin_del_juego = True  
    else:
        letras_erradas += intento
                    
    if len(letras_erradas) == len(HANGMAN_PICS):
        print("Se han acabado los intentos...\nLa palabra era '" + palabra + "'.")
        fin_del_juego = True
        
    print()
    
    if fin_del_juego:
        if play_again():
            palabra = obtener_palabra_aleatoria(lista_de_palabras)
            palabra = replace_vocals(palabra)
            letras_erradas = ''
            letras_correctas = ''
            letras_intentadas = ''
            fin_del_juego = False
            print('\n'*3)
        else:
            print("\nGracias por jugar\n")
            break