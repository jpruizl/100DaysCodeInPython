# 100 Day's Code In Python
# Day 008
# Juego de Ahorcado.

import random

# Lista de palabras posibles
palabras = ["python", "programacion", "juego", "ahorcado", "modularidad"]


# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)


# Función para mostrar el estado del ahorcado
def mostrar_ahorcado(intentos):
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    print(estados[intentos])


# Función para mostrar el estado actual de la palabra
def mostrar_palabra(palabra, letras_adivinadas):
    estado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    print("Palabra:", estado.strip())


# Función para jugar una partida de ahorcado
def jugar():
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 0
    max_intentos = 6

    print("¡Bienvenido al juego de Ahorcado!")
    print("Tienes que adivinar la palabra antes de que el ahorcado sea completado.")

    while intentos < max_intentos:
        mostrar_ahorcado(intentos)
        mostrar_palabra(palabra, letras_adivinadas)

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            intentos += 1
            print("La letra no está en la palabra.")

        if all(letra in letras_adivinadas for letra in palabra):
            print("¡Felicidades! Has adivinado la palabra.")
            mostrar_palabra(palabra, letras_adivinadas)
            break
    else:
        mostrar_ahorcado(intentos)
        print(f"Lo siento, has perdido. La palabra era '{palabra}'.")


# Iniciar el juego
continuar_jugando = True
while continuar_jugando:
    jugar()
    jugar_de_nuevo = input("¿Deseas jugar de nuevo? (si/no): ").lower()
    if jugar_de_nuevo != "si":
        continuar_jugando = False

print("Gracias por jugar. ¡Hasta luego!")