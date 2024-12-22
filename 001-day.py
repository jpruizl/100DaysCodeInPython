# 100 Day´s Code In Python
# Day 001

"""
Programa: 🕹Juego de 🔘Piedra, 📃Papel o ✂Tijera
Se jugara 5 rondas, usuario vs máquina.
tres niveles de dificultad: prinpicipante, intermedio y avanzado.
principiante inician en igualdad de puntos cero a cero.
intermedio se da una ventaja de un punto de victoria a la máquina.
avanzado se da una ventaja de dos puntos de victoria a la máquina.
"""

import random

# Función para obtener la elección del usuario
def obtener_eleccion_usuario():
    eleccion = input("Ingrese su elección (piedra, papel o tijera): ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        eleccion = input("Entrada NO válida, Ingrese su elección (piedra, papel o tijera):").lower()
    return eleccion


# Función para obtener la elección de la máquina
def obtener_eleccion_maquina():
    return random.choice(["piedra", "papel", "tijera"])


# Función para determinar el ganador de una ronda
def determinar_ganador(usuario, maquina):
    if usuario == maquina:
        return "empate"
    elif (usuario == "piedra" and maquina == "tijera") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):
        return "usuario"
    else:
        return "maquina"


# Función principal para jugar una partida
def jugar_partida(nivel):
    puntos_usuario = 0
    puntos_maquina = nivel # la ventaja inicial
    
    rondas = 5
    for _ in range(rondas):
        eleccion_usuario = obtener_eleccion_usuario()
        eleccion_maquina = obtener_eleccion_maquina()
        print(f"La máquina eligió: {eleccion_maquina}")
        
        ganador = determinar_ganador(eleccion_usuario, eleccion_maquina)
        if ganador == "usuario":
            puntos_usuario += 1
            print("!Ganaste esta ronda!")
        elif ganador == "maquina":
            puntos_maquina += 1
            print("La máquina ganó esta ronda.")
        else:
            print("Empate en esta ronda.")
        
        print(f"Puntuacuón - Usuario: {puntos_usuario}, Máquina: {puntos_maquina}")
        print("-" * 30)
        
    if puntos_usuario > puntos_maquina:
        print()
        print("!Ganaste la partida!")
    elif puntos_maquina > puntos_usuario:
        print()
        print("La máquina ganó la partida.")
    else:
        print()
        print("La partida terminó en empate.")



# Función para seleccionar el nivel de dificultad
def seleccionar_nivel():
    nivel = input("Seleccione el nivel de dificultad (principiante, intermedio, avanzado): ").lower()
    print()
    while nivel not in ["principiante", "intermedio", "avanzado"]:
        nivel = input("Entrada NO válida. Seleccione el nivel de dificultad (principiante, intermedio, avanzado): ").lower()
    
    if nivel == "principiante":
        return 0
    elif nivel == "intermedio":
        return 1
    elif nivel == "avanzado":
        return 2


# Programa Principal
print()
print("Bienvenido a nuestro 🕹Juego de 🔘Piedra, 📃Papel o ✂Tijera")
print("Reglas:")
print("Jugaras 5 partidas.")
print("por partida ganada acumlas 1 punto.")
print("Empate acumulas 0 puntos.")
print("Al finalizar se muestra los puntos acumulados")
print()
print("Puedes jugar en los niveles: principiante, intermedio y avanzado.")
print("principiante inician 0 a 0")
print("intermedio la máquina tiene una ventaja de 1 victoria.")
print("avanzado la máquina tiene una ventaja de 2 victorias.")
print("!!INICIEMOS!!")
print()
continuar_jugando = True
while continuar_jugando:
    nivel = seleccionar_nivel()
    jugar_partida(nivel)
    
    print()
    jugar_de_nuevo = input("¿Desea jugar de nuevo? (Si/No): ").lower()
    if jugar_de_nuevo != "si":
        continuar_jugando = False

print("Gracias por jugar con JuanpaGeek Games !!!")