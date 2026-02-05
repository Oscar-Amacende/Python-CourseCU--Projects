nombre = "Santiago"
nivel = "Avanzado"
edad_astronauta = 24
destino = "Venus"
combustible = 79
velocidad = 400

print ("Nombre del alumno: ", input("Introsuce tu nombre: "))
print (f"Nivel de conocimiento sobre python: {input('Introduce tu nivel de conocimiento: ')}\n")

print ("Hola Oscar, bienvenido al curso de python.")
print ("Tu conocimiento es avanzado, comenzaremos por la clase 1.")

print ("El nombre del profesor es: ", nombre)
print ("Su nivel es: ", nivel)

nombre = input ("Introduce tu nombre")
print (nombre)
print (f"Hola, soy",nombre,"Tengo:",edad_astronauta,"años y mi próximo destino es",destino)
print ("Estoy navegando a",velocidad,"Km/s con",combustible,"% de combustible restante hacia",destino)

┌──(admin㉿Huawei)-[~/Python]
└─$ cat ejercicio4.py
#datos complejos

# Listas en python

list = ["tarea1", "tarea2", "tarea3", [1,2,3,4,5]]
print (list)

# tuplas en python (Inmutable, no se puede modificar)

tupla = ("Tarea4", "tarea5", "tarea6")
print (tupla)

#Diccionarios elementos pares clave : valor en una tupla

diccionario = {
        #El elemento de diccionario no puede cambiar
        #El valor de una palabra de diccionario puede ser lo que sea
        "tarea1": [1,3,4,5],
        "tarea2": "en proceso",
        "tarea3": "Terminada"
    }

print (diccionario)

#Indexacion accerder a elementos de la cadena mediante el uso de un indice numerico tuplas

print(list[0])  #Primer elemento
print(list[-1]) #Ultimo elemento

#Indexacion de un elemento dentro del elemento seleccionado

print(list[1][1])
print(tupla[1])

#Indexacion de un diccionario, imprime el estado del complemento del diccionario

print(diccionario["tarea2"]);

#Slicing (Extraer subcadenas de una cadena de valores solo a listas)

print(list[:3]) #Saca del inicio hasta n
print(list[1:]) #Saca hasta el final
print(list[1:3]) #Se le suma uno al elemento final que quiere imprimir

#Stride (Extraer elementos no consecutivos)

print(list[0::2]) #Hace un salto de dos

#Modificacion de elementos, solo se pueden modificar las listas

list[2] = "Tarea especial"
print (list)


#Modificacion de diccionarios
diccionario["tarea2"] = "terminada"
print (diccionario)
