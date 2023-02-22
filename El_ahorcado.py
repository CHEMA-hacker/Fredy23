import random
import string

def obtener_palabra_válida(palabras):
   
    palabras = ["transformador", "carretera", "mototaxista"]

    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()
    

def ahorcado():

    print("Hi, Welcome the game")
    palabras = ["transformador", "carretera", "mototaxista"]

    palabra = obtener_palabra_válida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas= 5

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas)
        print(f"palabras: {' '.join(palabra_lista)}")

        letra_usuario = input("escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1





                print(f"\nTu letra, {letra_usuario} no está en la palabra. ")

        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. por favor ingresa otra letra.")
        else:
            print("\nEsta letra no es válida.")

    if vidas == 0:
        print(f"has perdido, la palabra era: {palabra}")
    else:
        print("has ganado. felicitaciones, estaba demasiado facil")



ahorcado()