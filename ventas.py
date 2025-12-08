# ventas.py
from data_manager import guardar_inventario

def registrar_venta(inventario):
    print("\n=== REGISTRAR VENTA ===")
    codigo = input("Código: ").strip()
    if codigo not in inventario:
        print("No existe ese código.")
        return

    p = inventario[codigo]
    try:
        cant = int(input("Cantidad vendida: "))
    except:
        print("Cantidad inválida.")
        return
    if cant <= 0:
        print("La cantidad debe ser mayor a cero.")
        return
    if cant > p["cantidad"]:
        print("Stock insuficiente.")
        return

    p["cantidad"] -= cant
    p["vendidos"] += cant
    guardar_inventario(inventario)
    print("✔ Venta registrada.")
