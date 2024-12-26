import random

#elementos = ("piedra","papel","tijera")

#ia = print(random.choice(elementos))

nombre1 = input("Nombre del Jugador 1: ")
nombre2 = input("Nombre del Jugador 2: ")

jugador1 = input(print("Hola ", nombre1, " ¿Qué elegirás? ¿Piedra, papel o tijeras?: "))
jugador2 = input(print("Hola ", nombre2, " ¿Qué elegirás? ¿Piedra, papel o tijeras?: "))

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ganador:", nombre1)
else:
    print("Ganador:", nombre2)
    