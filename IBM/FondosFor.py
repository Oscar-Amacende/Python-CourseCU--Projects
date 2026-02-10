inventario = [("Nmap",50,0.5), ("Wireshark",30,0.3), ("Metasploit",20,0.4) ,("BurpSuite",15,0.45)]
valor_total = 0

mayor_cantidad = {
    "herramienta": "",
    "cantidad": 0,
    "precio": 0
}

for herramienta, cantidad, precio in inventario:
    valor_total += cantidad * precio
    if cantidad > mayor_cantidad["cantidad"] :
        mayor_cantidad["herramienta"] = herramienta
        mayor_cantidad["cantidad"] = cantidad
        mayor_cantidad["precio"] = precio
        
#valor_total += valor_total
print (f"Valor total del inventario: {valor_total} eur")
print (f"Herramienta con mayor cantidad de licencias: {mayor_cantidad['herramienta']} ({mayor_cantidad['cantidad']} unidades)")

#Parte 2

compra = {
    "Nmap" : 5,
    "Wireshark" : 3,
    "Metasploit" : 0,
    "BurpSuite" : 0,
}

precio_total = 0;

# Usamos un diccionario de precios para buscar
precios_dict = {item[0] : item[2] for item in inventario}

# Usamos .item para obtener clave valor
for herramienta, cantidad in compra.items():
    if herramienta in precios_dict :
        precio = precios_dict[herramienta]
        precio_total += cantidad * precio

print(f"Precio total de la compra = {precio_total} eur")
