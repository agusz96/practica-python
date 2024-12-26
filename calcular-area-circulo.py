# Paso 1: Solicitar al usuario que ingrese el radio del círculo.

from math import pi

radio = float(input("Por favor ingrese el radio del círculo: "))

# Paso 2: Calcular el área del círculo utilizando la fórmula area = pi * radio^2

area = pi * (radio**2)

# Paso 3: Mostrar al usuario el área calculada del círculo.

print("El área del círculo con radio", radio, "es:", area)