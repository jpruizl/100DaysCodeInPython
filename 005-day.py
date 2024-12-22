# 100 Day's Code In Python
# Day 005
# Simulador a movimientos de un inventario.


def mostrar_productos(inventario):
    """Muestra la lista de productos en el inventario."""
    
    if not inventario:
        print("El inventario está vacío.")
        print()
        return
    
    print("\n--- Inventario ---")
    print("Código\tDescripción\tCategoría\tExistencia\tMín.\tMáx.\tPrecio\tCosto")
    for codigo, producto in inventario.items():
        print(f"{codigo}\t{producto['descripcion']}\t{producto['categoria']}\t{producto['existencia']}\t{producto['existencia_minima']}\t{producto['existencia_maxima']}\tQ{producto['precio']:.2f}\tQ{producto['costo']:.2f}")


def agregar_producto(inventario):
    """Agregar un nuevo producto al inventario."""
    
    codigo = input("Ingrese el código del producto: ")
    if codigo in inventario:
        print("El codigo ya existe en el inventario.")
        print()
        return
    
    descripcion = input("Ingrese la descripción del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    existencia = int(input("Ingrese la existencia inicial del producto: "))
    existencia_minima = int(input("Ingrese la existencia mínima del producto: "))
    existencia_maxima = int(input("Ingrese la existencia máxima del producto: "))
    precio = float(input("Ingrese el precio de venta del producto: "))
    costo = float(input("Ingrese el costo del producto: "))
    print()
    
    inventario[codigo] = {
        "descripcion": descripcion,
        "categoria": categoria,
        "existencia": existencia,
        "existencia_minima": existencia_minima,
        "existencia_maxima": existencia_maxima,
        "precio": precio,
        "costo": costo
    }
    
    print("Producto agregado exitosamente.")
    print()
    

def actualizar_existencia(inventario):
    """Actualiza la existencia de un producto en el inventario."""
    
    codigo = input("Ingrese el código del producto a actualizar: ")
    if codigo not in inventario:
        print("El código no existe en el inventario.")
        print()
        return
    
    nueva_existencia = int(input("Ingrese la nueva existencia del producto: "))
    if nueva_existencia < 0:
        print("La existencia no puede ser negativa.")
        print()
        return
    
    inventario[codigo]["existencia"] = nueva_existencia
    print("Existencia actualizada exitosamente.")
    print()


def movimiento_almacen(inventario):
    """Simula un moviemnto de productos entre almacenes."""
    
    codigo = input("Ingrese el código del producto a mover: ")
    if codigo not in inventario:
        print("El código no existe en el inventario.")
        print()
        return
    
    cantidad = int(input("Ingrese la cantidad a mover: "))
    if cantidad <= 0 or cantidad > inventario[codigo]["existencia"]:
        print("Cantidad inválida.")
        print()
        return
    
    almacen_origen = input("Ingrese el almacén de origen (A o B): ")
    almacen_destino = input("Ingrese el almacén de destino (A o B): ")
    if almacen_origen not in ["A", "B"] or almacen_destino not in ["A", "B"] or almacen_origen == almacen_destino:
        print("Almacenes inválidos.")
        return
    
    inventario[codigo]["existencia"] -= cantidad
    print(f"Movimiento de {cantidad} {inventario[codigo]["descripcion"]}(s) de {almacen_origen} a {almacen_destino} realizado.")
    print()


def menu(inventario):
    """Muestra el menú y gestiona las opciones del usuario."""
    
    while True:
        print("\n--- Menú ---")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Actualizar existencia")
        print("4. Movimiento entre almacenes")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        print()
        
        if opcion == "1":
            mostrar_productos(inventario)
        elif opcion == "2":
            agregar_producto(inventario)
        elif opcion == "3":
            actualizar_existencia(inventario)
        elif opcion == "4":
            movimiento_almacen(inventario)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            print()


if __name__ == "__main__":
    inventario = {}  # diccionario para almacenar los productos
    print()
    menu(inventario)
    print()
    print("Gracias por usar nuestras soluciones")
    print("JuanpaGeek Developer")
