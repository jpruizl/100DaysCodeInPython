# 100 Day's Code In Python
# Day 006
# Ficha manejo de paciente en clinica médica.

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    """Calcula la edad del paciente a partir de su fecha de nacimiento."""

    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def mostrar_paciente(paciente):
    """Muestra los datos del paciente."""

    print("\n--- Datos del Paciente ---")
    print(f"Nombre: {paciente['nombre']}")
    print(f"Fecha de Nacimiento: {paciente['fecha_nacimiento'].strftime('%d/%m/%Y')}")
    print(f"Edad: {calcular_edad(paciente['fecha_nacimiento'])} años")
    
    # Mostrar otras secciones si existen datos
    if 'recetas' in paciente and paciente['recetas']:
        print("\nRecetas:")
        for receta in paciente['recetas']:
            print(f"- {receta}")

    if 'medicamentos' in paciente and paciente['medicamentos']:
        print("\nMedicamentos:")
        for medicamento in paciente['medicamentos']:
            print(f"- {medicamento}")

    if 'laboratorios' in paciente and paciente['laboratorios']:
        print("\nLaboratorios:")
        for laboratorio in paciente['laboratorios']:
            print(f"- {laboratorio}")

    if 'historial_cirugias' in paciente and paciente['historial_cirugias']:
        print("\nHistorial de Cirugías:")
        for cirugia in paciente['historial_cirugias']:
            print(f"- {cirugia}")

def agregar_receta(paciente):
    """Agrega una nueva receta al historial del paciente."""

    receta = input("Ingrese la descripción de la receta: ")
    paciente['recetas'].append(receta)
    print("Receta agregada exitosamente.")

def agregar_medicamento(paciente):
    """Agrega un nuevo medicamento a la lista del paciente."""

    medicamento = input("Ingrese el nombre del medicamento: ")
    paciente['medicamentos'].append(medicamento)
    print("Medicamento agregado exitosamente.")

def agregar_laboratorio(paciente):
    """Agrega un nuevo laboratorio al historial del paciente."""

    laboratorio = input("Ingrese la descripción del laboratorio: ")
    paciente['laboratorios'].append(laboratorio)
    print("Laboratorio agregado exitosamente.")

def agregar_cirugia(paciente):
    """Agrega una nueva cirugía al historial médico del paciente."""

    cirugia = input("Ingrese la descripción de la cirugía: ")
    paciente['historial_cirugias'].append(cirugia)
    print("Cirugía agregada al historial médico.")

def menu(paciente):
    """Muestra el menú principal y gestiona las opciones del usuario."""

    while True:
        print("\n--- Menú ---")
        print("1. Mostrar datos del paciente")
        print("2. Agregar receta")
        print("3. Agregar medicamento")
        print("4. Agregar laboratorio")
        print("5. Agregar cirugía al historial médico")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_paciente(paciente)
        elif opcion == '2':
            agregar_receta(paciente)
        elif opcion == '3':
            agregar_medicamento(paciente)
        elif opcion == '4':
            agregar_laboratorio(paciente)
        elif opcion == '5':
            agregar_cirugia(paciente)
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    # Datos iniciales del paciente (puedes obtenerlos del usuario o de una base de datos)
    paciente = {
        "nombre": "Juan Pérez",
        "fecha_nacimiento": datetime(1990, 5, 12),
        "recetas": [],
        "medicamentos": [],
        "laboratorios": [],
        "historial_cirugias": []
    }

    menu(paciente)