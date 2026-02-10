alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cifrado_cesar(texto, desplazamiento):
    i = 0
    iter = 0
    #Variable para el texto cifrado
    texto_cifrado = " "

    
    for caracter in texto :
        #Imprime hola
        #print(caracter)
        
        if caracter in alfabeto:
            #print(f"Contiene {caracter}")
            #print(alfabeto.index(caracter))
            nvoindice = alfabeto.index(caracter) + desplazamiento
            print(alfabeto[nvoindice])
        #i += desplazamiento
        iter += 1
        
    if caracter not in alfabeto :
        print("Tu caracter no está en el alfabeto")
    
    
    #for i in range(len(alfabeto)) :
        #Imprime el alfabeto
        #print(alfabeto[i])

    #i+= 1
    #print(texto)
    #print(desplazamiento)

a = cifrado_cesar("HOLA MUNDO",1)
