import math

print("Calculadora Básica en Python")

def suma(n1,n2):
    s=n1+n2
    print (s,"\n")

def resta(n1,n2):
    r=n1-n2
    print (r,"\n")

def mult(n1,n2):
    m=n1*n2;
    print (m,"\n")

def div(n1,n2):
    d=n1/n2;
    if d == 0: 
        print ("Error, op no valida")
    else: 
        print(d,"\n")

def menu ():
    print("----Calculadora----")
    print("1-.Suma")
    print("2-.Resta")
    print("3-.Multiplicación")
    print("4-.División")

while True:
    menu()

    opera = int(input("Ingresa el numero de Operación: "))
    if opera == 1:

        print("Suma")
        n1=int(input("Ingrese n1:"))
        n2=int(input("Ingrese n2:"))
        suma(n1,n2)

    elif opera == 2:

        print("resta")
        n1=int(input("Ingrese n1:"))
        n2=int(input("Ingrese n2:"))
        resta(n1,n2)

    elif opera == 3:

        print("Multiplicacion")
        n1=int(input("Ingrese n1:"))
        n2=int(input("Ingrese n2:"))
        mult(n1,n2)

    elif opera == 4:

        print("Division")
        n1=int(input("Ingrese n1:"))
        n2=int(input("Ingrese n2:"))
        div(n1,n2)

else: 
    print("hola")
