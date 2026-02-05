password = "Testpass1234"
#true o false
longitud = len(password)
longitud >= 8

caracter= ('@' not in password and '#' not in password)

buscando_digitos = [caracter.isdigit() for caracter in password]
numero = (any(buscando_digitos))

espacios = (' ' not in password )

print("Contraseña:",password)
print("¿La contraseña cumple con los criterios establecidos?",longitud and caracter and buscando_digitos and numero and espacios)
