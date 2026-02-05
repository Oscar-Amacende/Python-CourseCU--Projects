def menu():
    print("----Pizzeria Bella Napoli----")
    print("1-.Pizza Vegetariana")
    print("2-.Pizza Clasica")

def submenuV():
    print("1-.Pimiento")
    print("2-.Tofu")

def submenuC():
    print("1-. Peperoni")
    print("2-. Jamon")
    print("3-. Salmon")

while True:
    menu()

    opc = int(input("Elija una pizza:"))
    if opc == 1:
        submenuC()
    elif opc ==2:
        submenuV()
    else:
        print("Por favor elija una opcion valida")
