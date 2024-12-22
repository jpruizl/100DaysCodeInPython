# 100 Day's Code In Python
# Day 007
# Monitoreo o simulador de accesos de nivel de usuario

# Función para crear un usuario con nivel de acceso y contraseña
def crear_usuario():
    print("Creando un nuevo usuario...")
    nombre = input("Ingrese el Nombre del usuario: ")
    nivel_acceso = int(input("Ingrese el Nivel de Acceso (1: Total, 2: Médio, 3: Restringido): "))
    constraseña = input("Ingrese la Contraseña para el usuario: ")
    print(f"Usuario {nombre} creado exitosamente con el nivel de acceso {nivel_acceso}.")
    return nombre, nivel_acceso, constraseña


# Función para verificar el nivel de acceso
def verifica_acceso(nivel_acceso):
    print("\nVerificando nivel de acceso...")
    if nivel_acceso == 1:
        print("Acceso total: Tienes acceso a todas las áreas del programa.")
    elif nivel_acceso == 2:
        print("Acceso medio: Tienes acceso a algunas áreas del programa.")
    elif nivel_acceso == 3:
        print("Acceso restringido: Tienes acceso limitado al programa.")    
    else:
        print("Nivel de acceso no válido.")


# Función para restablecer la contraseña
def restablecer_contraseña(nombre, contraseña_actual):
    print("\nRestableciendo la contraseña...")
    intento_nombre = input("Ingrese el nombre de usuario: ")
    if intento_nombre == nombre:
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        confirmar_contraseña = input("Confirme la nueva contraseña: ")
        if nueva_contraseña == confirmar_contraseña:
            print("Contraseña restablecida exitosamente.")
            return nueva_contraseña
        else:
            print("Las contraseñas no coinciden. Intente de nuevo.")
            return contraseña_actual
    else:
        print("EL nombre de usuario no coincide. No se puede restablecer la contraseña.")
        return contraseña_actual


# Función principal del programa
def main():
    nombre, nivel_acceso, contraseña = crear_usuario()
    verifica_acceso(nivel_acceso)
    
    while True:
        print("\nOpciones:")
        print("1. Verificar acceso")
        print("2. Cambiar contraseña")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            verifica_acceso(nivel_acceso)
        elif opcion == "2":
            contraseña = restablecer_contraseña(nombre, contraseña)
        elif opcion == "3":
            print("Saliendo del programa...")
            break   
        else:
            print("Opción no válida, intente de nuevo.")
        

# Ejecutar el programa
if __name__ == '__main__':
    main()
    