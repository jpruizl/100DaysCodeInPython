# 100 Day´s Code In Python
# Day 003
# Simulador Carrito de compras.

def mostrar_productos(productos):
    """Muestra la lista de productos disponibles con sus precios."""
    
    print("\n---Productos disponibles---")
    for i, (producto, precio) in enumerate(productos.items()):
        print(f"{i + 1}. {producto}: Q{precio:.2f}")


def agregar_producto(carrito, productos):
    """Agrega un producto al carrito de compras."""
    
    mostrar_productos(productos)
    
    while True:
        try:
            opcion = int(input("Seleccione el número del producto a agregar:")) - 1
            if 0 <= opcion < len(productos):
                producto = list(productos.keys()) [opcion]
                cantidad = int(input(f"Ingrese la cantidad de {producto} a agregar: "))
                if cantidad > 0:
                    if producto in carrito:
                        carrito[producto] += cantidad
                    else:
                        carrito[producto] = cantidad
                    print(f"{cantidad} {producto}(s) agregado(s) al carrito.")
                    break
                else:
                    print("La cantidad debe ser mayor a cero.")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")
    
    
def quitar_producto(carrito):
    """Quitar un producto del carrito de compras."""
    
    if not carrito:
        print("El carrito está vació.")
        return
    
    print("\n--- Productos en el carrito ---")
    for i, (producto, cantidad) in enumerate(carrito.items()):
        print(f"{i + 1}. {producto}: {cantidad}")
    
    while True:
        try:
            opcion = int(input("Seleccione el número del producto a quitar: ")) - 1
            if 0 <= opcion < len(carrito):
                producto = list(carrito.keys()) [opcion]
                del carrito[producto]
                print(f"{producto} eliminado del carrito.")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")


def modificar_cantidad(carrito):
    """Modifica la cantidad de un producto en el carrito."""
    
    if not carrito:
        print("El carrito está vácio.")
        return
    
    print("\n--- Productos en el carrito ---")
    for i, (producto, cantidad) in enumerate(carrito.items()):
        print(f"{i + 1}. {producto}: {cantidad}")
    
    while True:
        try:
            opcion = int(input("Seleccione el número del producto a modificar: ")) - 1
            if 0 <= opcion < len(carrito):
                producto = list(carrito.keys()) [opcion]
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {producto}: "))
                if nueva_cantidad > 0:
                    carrito[producto] = nueva_cantidad
                    print(f"Cantidad de {producto} actualizada a {nueva_cantidad}.")
                    break
                else:
                    print("La cantidad debe ser mayor a cero.")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")


def calcular_total(carrito, productos):
    """Calcula el total de la compra, incluyendo impuestos."""
    
    subtotal = 0
    for producto, cantidad in carrito.items():
        subtotal += productos[producto] * cantidad
    
    impuestos = subtotal * 0.12
    total = subtotal + impuestos
    return subtotal, impuestos, total


def mostrar_factura(carrito, productos):
    """Muestra la factura de la compra."""
    
    if not carrito:
        print("El carrito está vácio. No hay factura a mostrar.")
        return
    
    subtotal, impuestos, total = calcular_total(carrito, productos)
    
    print("\n--- Factura ---")
    for producto, cantidad in carrito.items():
        precio_unitario = productos[producto]
        precio_total = precio_unitario * cantidad
        print(f"{producto} x {cantidad}: Q{precio_total:.2f}")
    
    print(f"Subtotal: Q{subtotal:.2f}")
    print(f"Impuestos (12%): Q{impuestos:.2f}")
    print(f"Total a pagar: Q{total:.2f}")


def menu(productos):
    """Muestra el menú principal y gestiona las opciones del usuario."""
    
    carrito = {}
    
    while True:
        print("\n--- Menú ----")
        print("1. Ver productos")
        print("2. Agregar producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Modificar cantidad de producto en el carrito")
        print("5. Ver factura")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(carrito, productos)
        elif opcion == "3":
            quitar_producto(carrito)
        elif opcion == "4":
            modificar_cantidad(carrito)
        elif opcion == "5":
            mostrar_factura(carrito, productos)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")


# Programa Principal
if __name__ == "__main__":
    productos = {
        "Camisa": 50.00,
        "Pantalón": 80.00,
        "Zapatos": 120.00,
        "Gorra": 25.00
    }
    
    menu(productos)

