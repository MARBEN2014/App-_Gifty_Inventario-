
from data_manager import cargar_inventario, mostrar_ruta_excel
from menu import mostrar_menu
from crud import agregar_producto, actualizar_producto, eliminar_producto, mostrar_inventario, buscar_producto
from ventas import registrar_venta
from reportes import generar_reportes

def main():
    inventario = cargar_inventario()

    while True:
        mostrar_menu()
        op = input("\nOpción: ").strip()

        if op == "1":
            agregar_producto(inventario)
        elif op == "2":
            actualizar_producto(inventario)
        elif op == "3":
            eliminar_producto(inventario)
        elif op == "4":
            mostrar_inventario(inventario)
        elif op == "5":
            buscar_producto(inventario)
        elif op == "6":
            registrar_venta(inventario)
        elif op == "7":
            generar_reportes(inventario)
        elif op == "8":
            print("Saliendo... Muchas gracias por usar Gifty.")
            break
        elif op == "9":
            mostrar_ruta_excel()
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
