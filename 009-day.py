""" Día 009 - Reto Python
100 Days of Code with Python
Adivininanza de números"""

import random
import time

def generar_numero_secreto(digitos):
    """Genera un número aleatorio con la cantidad de digitos especificada"""
    inicio = 10 ** (digitos - 1)
    fin = (10 ** digitos) - 1
    return random.randint(inicio, fin)


def obtener_pista(numero_secreto, intento):
    """Analiza el intento y devuelve pista sobre los digitos correctos"""
    numero_secreto_str = str(numero_secreto)
    intento_str = str(intento)
    
    if len(intento_str) != len(numero_secreto_str):
        return "EL número debe tener {} digitos".format(len(numero_secreto_str))
    
    digitos_correctos = 0
    posiciones_correctas = 0
    
    # Verificar digitos y posiciones correctas
    for i in range(len(numero_secreto_str)):
        if intento_str[i] == numero_secreto_str[i]:
            posiciones_correctas += 1
        elif intento_str[i] in numero_secreto_str:
            digitos_correctos += 1
    
    return f"Dígitos correctos: {digitos_correctos}, En posiciones correctas: {posiciones_correctas}"


def jugar_adivinanza():
    """Función principal del juego"""
    print("Bienvenido a la adivinanza de números")
    print("Estoy pensando en un número de 3 dígitos...")
    time.sleep(1)
    
    numero_secreto = generar_numero_secreto(3)
    intentos = 0
    tiempo_inicio = time.time()
    
    while True:
        try:
            intento = int(input("\nIngresa tu intento: "))
            intentos += 1
            
            if intento == numero_secreto:
                tiempo_total = round(time.time() - tiempo_inicio, 2)
                print(f"\n!Felicidades! !Has adivinado el número {numero_secreto}!")
                print(f"lo lograste en {intentos} intentos")
                print(f"y en un tiempo de: {tiempo_total} segundos!")
                break
            
            pista = obtener_pista(numero_secreto, intento)
            print(pista)
            
            if intentos % 3 == 0:
                print(f"\nPista adicional: La suma de los digitos y es {sum(int(d) for d in str(numero_secreto))}")
        
        except ValueError:
            print("Por favor, ingresa un número valido")
        
            

if __name__ == "__main__":
    while True:
        jugar_adivinanza()
        if input("\n¿Quieres jugar de nuevo? (s/n): ").lower() != "s":
            print("¡Gracias por jugar!")
            break