# reportes.py
def generar_reportes(inventario):
    print("\n===== REPORTES =====")
    print(f"\nTotal de productos: {len(inventario)}")
    print(f"Total unidades: {sum(p['cantidad'] for p in inventario.values())}")

    print("\nProductos con stock bajo (< 100):")
    for p in inventario.values():
        if p["cantidad"] < 100:
            print(f" - {p['nombre']}: {p['cantidad']}")

    print("\nTop 5 más vendidos:")
    top = sorted(inventario.values(), key=lambda x: x["vendidos"], reverse=True)[:5]
    for p in top:
        print(f" - {p['nombre']} | Vendidos: {p['vendidos']}")
