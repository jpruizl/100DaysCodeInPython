# Day 11
# Generador de Matrices en Espiral

def crear_matriz_espiral(n):
    """Crea una matriz de nxn con números en espiral"""
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    inicio_fila = inicio_col = 0
    fin_fila = fin_col = n - 1
    
    while inicio_fila <= fin_fila and inicio_col <= fin_col:
        # Derecha
        for i in range(inicio_col, fin_col + 1):
            matriz[inicio_fila][i] = valor
            valor += 1
        inicio_fila += 1
        
        # Abajo
        for i in range(inicio_fila, fin_fila + 1):
            matriz[i][fin_col] = valor
            valor += 1
        fin_col -= 1
        
        if inicio_fila <= fin_fila:
            # Izquierda
            for i in range(fin_col, inicio_col - 1, -1):
                matriz[fin_fila][i] = valor
                valor += 1
            fin_fila -= 1
        
        if inicio_col <= fin_col:
            # Arriba
            for i in range(fin_fila, inicio_fila - 1, -1):
                matriz[i][inicio_col] = valor
                valor += 1
            inicio_col += 1
    
    return matriz


def mostrar_matriz_ascii(matriz):
    """Muestra la matriz con bordes ASCII"""
    n = len(matriz)
    # Encuentra el número más grande para el padding
    max_width = len(str(n * n))
    
    # Borde superior
    print('┌' + '─' * (n * (max_width + 1) + 1) + '┐')
    
    # Contenido de la matriz
    for fila in matriz:
        print('|', end=' ')
        for num in fila:
            print(f"{num:>{max_width}}", end=' ')
        print('|')
    
    # Borde inferior
    print('└' + '─' * (n * (max_width + 1) + 1) + '┘')


def animar_creacion_matriz(n):
    """Muestra la creación de la matriz paso a paso"""
    import time
    import os
    
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    inicio_fila = inicio_col = 0
    fin_fila = fin_col = n - 1
    
    def mostrar_estado():
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_matriz_ascii(matriz)
        time.sleep(0.1)
    
    while inicio_fila <= fin_fila and inicio_col <= fin_col:
        # Mismo patrón de crear_matriz_espiral pero con animación
        # Derecha
        for i in range(inicio_col, fin_col + 1):
            matriz[inicio_fila][i] = valor
            valor += 1
            mostrar_estado()
        inicio_fila += 1
        
        # Abajo
        for i in range(inicio_fila, fin_fila + 1):
            matriz[i][fin_col] = valor
            valor += 1
            mostrar_estado()
        fin_col -= 1
        
        if inicio_fila <= fin_fila:
            # Izquierda
            for i in range(fin_col, inicio_col - 1, -1):
                matriz[fin_fila][i] = valor
                valor += 1
                mostrar_estado()
            fin_fila -= 1
        
        if inicio_col <= fin_col:
            # Arriba
            for i in range(fin_fila, inicio_fila - 1, -1):
                matriz[i][inicio_col] = valor
                valor += 1
                mostrar_estado()
            inicio_col += 1
            

def main():
    while True:
        print("\n=== GENERADOR DE MATRIZ ESPIRAL ===")
        print("1. Generar matriz")
        print("2. Ver animación de creación")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == "1":
            try:
                n = int(input("Ingrese el tamaño de la matriz (n): "))
                if n > 0:
                    matriz = crear_matriz_espiral(n)
                    mostrar_matriz_ascii(matriz)
                else:
                    print("Por favor ingrese un número positivo")
            except ValueError:
                print("Por favor ingrese un número válido")
                
        elif opcion == "2":
            try:
                n = int(input("Ingrese el tamaño de la matriz (n): "))
                if n > 0:
                    animar_creacion_matriz(n)
                else:
                    print("Por favor ingrese un número positivo")
            except ValueError:
                print("Por favor ingrese un número válido")
        
        elif opcion == "3":
            print("!Hasta luego!")
            break
        
        else:
            print("Opción no válido")


# Programa principal
if __name__ == "__main__":
    main()