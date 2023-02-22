def arbol(pisos):

    resultado=[" "*(pisos-i)+"*"*(i+i-1) for i in range(1,pisos+1)]
    return "\n".join(resultado)
 
numero=int(input("dime un número: "))
print(arbol(numero))