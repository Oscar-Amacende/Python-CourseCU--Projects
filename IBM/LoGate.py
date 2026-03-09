# Verifiquemos si un número NO está (entre 1 y 10)
number = 15

# Estas dos expresiones son equivalentes:
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number <= 10)

print(result1)  # Verdadero
print(result2)  # Verdadero
