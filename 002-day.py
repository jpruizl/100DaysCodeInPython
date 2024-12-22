# 100 Day´s Code In Python
# Day 002

"""
Programa: Simulador Manejador de Contraseñas.
CRUD para Manejo de contraseñas a un usuario creado.
C = Create ->
R = Read ->
U = Update ->
D = Delete ->
"""

def solicitar_credenciales():
    """Solicita al usuario su nombre de usuario y contraseña."""
    
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    return usuario, contrasena


def almacenar_credenciales(usuario, contrasena, credenciales):
    """Almacena las credenciales en un diccionario"""
    
    credenciales[usuario] = contrasena
    print("Credenciales almacenadas exitosamente.")


def cambiar_contrasena(credenciales):
    """Permite al usuario cambiar su contraseña"""
    
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in credenciales:
        nueva_contrasena = input("Ingrese su nueva contraseña: ")
        credenciales[usuario] = nueva_contrasena
        print("Contraseña cambiada exitosamente.")
    else:
        print("Usuario no encontrado.")


def eliminar_credenciales(credenciales):
    """Elimina las credenciales  un usuario."""
    
    usuario = input("Ingrese el nombre de usuario a eliminar: ")
    if usuario in credenciales:
        del credenciales[usuario]
        print("Credenciales eliminadas exitosamente.")
    else:
        print("Usuario no encontrado.")


def leer_credenciales(credenciales):
    """Muestra las credenciales almacenadas."""
    
    if credenciales:
        print("Credenciales almacenadas:")
        for usuario, contrasena in credenciales.items():
            print(f"Usuario: {usuario}, Contraseña: {contrasena}")
    else:
        print("No hay credenciales almancenadas.")


def menu():
    """Muestra el menú de opciones al usuario."""
    
    credenciales = {}  # Diccionario para almacenar las credenciales
    
    while True:
        print("--- Menú ---")
        print("1. Almacenar credenciales")
        print("2. Cambiar contraseña")
        print("3. Eliminar credenciales")
        print("4. Leer credenciales")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            usuario, contrasena = solicitar_credenciales()
            almacenar_credenciales(usuario, contrasena, credenciales)
        elif opcion == "2":
            cambiar_contrasena(credenciales)
        elif opcion == "3":
            eliminar_credenciales(credenciales)
        elif opcion == "4":
            leer_credenciales(credenciales)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

# Programa Principal
if __name__ == "__main__":
    menu()
    