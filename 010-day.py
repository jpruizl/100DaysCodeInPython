def contar_palabras(texto):
    """Cuenta la frecuencia cada palabra en el texto"""
    # Convertir a minúsculas y eliminar signos de puntuación básicas
    caracteres_especiales = ".,;:!¡¿?\"'()[]{}"
    for caracter in caracteres_especiales:
        texto = texto.replace(caracter, "")

    palabras = texto.lower().split()
    frecuencia = {}

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


def encontrar_palabras_mas_comunes(frecuencia, n=5):
    """Encuentra las n palabras más comunes"""
    return sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:n]


def analizar_longitud_palabras(texto):
    """Analiza la longitud promedio de palabras y encuentra la más larga"""
    palabras = texto.split()
    if not palabras:
        return 0, ""

    longitudes = [len(palabra) for palabra in palabras]
    promedio = sum(longitudes) / len(longitudes)
    palabra_mas_larga = max(palabras, key=len)

    return round(promedio, 2), palabra_mas_larga


def crear_informe_analisis(nombre_archivo):
    """ Crea un informe completo del análisis del texto"""
    try:
        # Leer el archivo
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        # Realizar análisis
        total_caracteres = len(texto)
        total_palabras = len(texto.split())
        frecuencia_palabras = contar_palabras(texto)
        palabras_comunes = encontrar_palabras_mas_comunes(frecuencia_palabras)
        promedio_longitud, palabra_mas_larga = analizar_longitud_palabras(texto)

        # Crear nombre para el archivo de reporte
        nombre_reporte = f"reporte_{nombre_archivo.split('.')[0]}.txt"

        # Escribir reporte
        with open(nombre_reporte, "w", encoding="utf-8") as reporte:
            reporte.write("===REPORTE DE ANÁLISIS DE TEXTO ===\n\n")
            reporte.write(f"Archivo analizado: {nombre_archivo}\n")
            reporte.write(f"Total de caracteres: {total_caracteres}\n")
            reporte.write(f"Total de palabras: {total_palabras}\n")
            reporte.write(f"Longitud promedio de palabras: {promedio_longitud}\n")
            reporte.write(f"Palabra más larga: {palabra_mas_larga}\n\n")

            reporte.write("Top 5 palabras más frecuentes:\n")
            for palabra, freq in palabras_comunes:
                reporte.write(f"- '{palabra}': {freq} veces\n")

        print(f"Reporte creado con éxito: {nombre_reporte}")
        return True

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return False
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return False


def main():
    while True:
        print("\n===ANALIZADOR DE TEXTO===")
        print("1. Analizar un archivo de texto")
        print("2. Salir")

        opcion = input("\nSeleccione una opción: (1-2): ")

        if opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo a analizar: ")
            crear_informe_analisis(nombre_archivo)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()