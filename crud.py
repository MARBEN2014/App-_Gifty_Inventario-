
from data_manager import guardar_inventario
from utils import ROJO, RESET

def agregar_producto(inventario):
    print("\n=== AGREGAR PRODUCTO ===")
    codigo = input("Código del producto: ").strip()
    if codigo in inventario:
        print("Ya existe un producto con ese código.")
        return

    nombre = input("Nombre del producto: ").strip()
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except:
        print("Dato inválido.")
        return

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "vendidos": 0
    }
    guardar_inventario(inventario)
    print("✔ Producto agregado.")

def actualizar_producto(inventario):
    print("\n=== ACTUALIZAR PRODUCTO ===")
    codigo = input("Código del producto: ").strip()
    if codigo not in inventario:
        print("No existe ese código.")
        return

    p = inventario[codigo]
    print(f"Nombre actual: {p['nombre']}")
    print(f"Precio actual: {p['precio']}")
    print(f"Cantidad actual: {p['cantidad']}")

    print("\n1. Cambiar nombre")
    print("2. Cambiar precio")
    print("3. Cambiar cantidad")
    print("4. Cancelar")
    op = input("Opción: ")

    if op == "1":
        p["nombre"] = input("Nuevo nombre: ").strip()
    elif op == "2":
        try:
            p["precio"] = float(input("Nuevo precio: "))
        except:
            print("Precio inválido.")
            return
    elif op == "3":
        try:
            p["cantidad"] = int(input("Nueva cantidad: "))
        except:
            print("Cantidad inválida.")
            return
    elif op == "4":
        return
    else:
        print("Opción inválida.")
        return

    guardar_inventario(inventario)
    print("✔ Producto actualizado.")

def eliminar_producto(inventario):
    print("\n=== ELIMINAR PRODUCTO ===")
    codigo = input("Código a eliminar: ").strip()
    if codigo not in inventario:
        print("No existe ese código.")
        return

    if input("¿Seguro? (s/n): ").lower() == "s":
        del inventario[codigo]
        guardar_inventario(inventario)
        print("✔ Producto eliminado.")
    else:
        print("Cancelado.")

def mostrar_inventario(inventario):
    print("\n=== INVENTARIO COMPLETO ===\n")
    if not inventario:
        print("Vacío.")
        return

    print(f"{'COD':<10}{'NOMBRE':<35}{'PRECIO':<12}{'CANT':<10}{'VENDIDOS':<10}")
    for cod, p in inventario.items():
        alerta = ROJO + "⚠ STOCK BAJO" + RESET if p["cantidad"] < 100 else ""
        print(f"{cod:<10}{p['nombre']:<35}${p['precio']:<11.2f}{p['cantidad']:<10}{p['vendidos']:<10} {alerta}")

def buscar_producto(inventario):
    print("\n=== BUSCAR PRODUCTO ===")
    termino = input("Código o nombre: ").lower().strip()
    encontrados = [(cod, p) for cod, p in inventario.items() if termino == cod.lower() or termino in p["nombre"].lower()]
    if not encontrados:
        print("No encontrado.")
        return
    for cod, p in encontrados:
        print(f"{cod} → {p['nombre']} | ${p['precio']} | Stock: {p['cantidad']}")
