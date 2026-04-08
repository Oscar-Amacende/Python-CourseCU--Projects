import string
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
caracteres = [" ",",",".",":"]

def cifrado_cesar(texto, desplazamiento):
    i = 0
    iter = 0
    texto_cifrado = ""

    for caracter in texto :
        
        if caracter in alfabeto:
            nvoindice = alfabeto.index(caracter) + desplazamiento
            nvoindice = nvoindice % len(alfabeto)
            texto_cifrado += alfabeto[nvoindice]
        elif caracter in caracteres:
            texto_cifrado += caracter
            #print(caracter)
        elif caracter.islower():
            try :
                raise ValueError 
            except ValueError:
                #print("")
                return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
                
        else :
            texto_cifrado += caracter
    #iter += 1
    return texto_cifrado
    
def descifrado_cesar(texto_cifrado, deslpazamiento):
    texto_descifrado = ""

    for caracter in texto_cifrado:
        if caracter in alfabeto:
            nvoindice1 = alfabeto.index(caracter) - deslpazamiento
            nvoindice1 = nvoindice1 % len(alfabeto)
            texto_descifrado += alfabeto[nvoindice1]
        elif caracter in caracteres :
            texto_descifrado += caracter
        else : 
            texto_descifrado += caracter
    return texto_descifrado
    


a = cifrado_cesar("hola mundo.",1)
print(a)
b = descifrado_cesar(a,1)
print(b)
