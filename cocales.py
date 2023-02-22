def contar_vocales(palabra_frase):

    contador_de_vocales = 0

    for letra in palabra_frase:
        if letra.lower() in "aeiou":
            contador_de_vocales += 1

    return contador_de_vocales

palabra = input("escribe una palabra o una frase corta: ")
cantidad_de_vocales = contar_vocales(palabra)
print(f"en la palabra o frase:  {palabra}, hay {cantidad_de_vocales} vocales")

if cantidad_de_vocales % 2 == 0:
     print(" y el número de vocales es par")
else:
     print(" y el número de vocales es impar")




