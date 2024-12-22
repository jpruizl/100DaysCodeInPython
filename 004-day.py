# 100 Day's Code In Python
# Day 004
# TO DO, de Tareas a Realizar.

from datetime import datetime

def agregar_tareas(tareas):
    """Agrega una nueva tarea a la lista."""
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite_str = input("Ingrese la fecha limite (formato DD/MM/AAAA): ")    
    fecha_limite = datetime.strptime(fecha_limite_str, "%d/%m/%Y")
    tareas.append({"descripcion": descripcion, "fecha_limite": fecha_limite, "completada": False})
    print("Tarea agregada exitosamente.")
    print()


def mostrar_tareas(tareas):
    """Muestra la lista de tareas."""
    if not tareas:
        print("No hay tareas pendientes.")
        print()
        return
    
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        fecha_limite_str = tarea["fecha_limite"].strftime("%d/%m/%Y")
        print(f"{i + 1}. {tarea['descripcion']} - Fecha Límite: {fecha_limite_str} - Estado: {estado}")
        print()


def marcar_completada(tareas):
    """Marca una tarea como completada."""  
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
        print()
    else:
        print("Indice inválido.")
        print()


def editar_tarea(tareas):
    """Edita la descripción o fecha límite de una tarea."""
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el número de la tarea a editar: ")) - 1
    if 0 <= indice < len(tareas):
        nueva_descripcion = input("Ingrese la nueva descripción (dejar en blanco para mantener la actual): ")
        nueva_fecha_limite_str = input("Ingrese la nueva fecha límite (formato DD/MM/AAAA. dejar en blanco para mantener la actual): ")
        
        if nueva_descripcion:
            tareas[indice]["descripcion"] = nueva_descripcion
        
        if nueva_fecha_limite_str:
            nueva_fecha_limite = datetime.strptime(nueva_fecha_limite_str, "%d/%m/%Y")
            tareas[indice]["fecha_limite"] = nueva_fecha_limite
        
        print("Tarea editada exitosamente.")
        print()
    else:
        print("Indice inválido.")
        print()


def eliminar_tarea(tareas):
    """Elimina una tarea de la lista."""
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        del tareas[indice]
        print("Tarea eliminada exitosamente.")
        print()
    else:
        print("Indice inválido.")
        print()


def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    tareas = []
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")
        
        print()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tareas(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            editar_tarea(tareas)
        elif opcion == "5":
            eliminar_tarea(tareas)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
            print()


if __name__ == "__main__":
    menu()
    print()
    print()
    print("Gracias por usar nuestras soluciones.")
    print("JuanpaGeek Developer.")
    print()
