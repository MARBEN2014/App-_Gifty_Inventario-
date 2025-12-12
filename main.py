
"""from data_manager import cargar_inventario, mostrar_ruta_excel
from menu import mostrar_menu
from crud import agregar_producto, actualizar_producto, eliminar_producto, mostrar_inventario, buscar_producto
# todas las funciones se importar con*
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
    main()"""
    
from data_manager import cargar_inventario, mostrar_ruta_excel
from menu import mostrar_menu
from crud import * 
""" otra forma de importar las fucniones del modulo Crud (
    agregar_producto,
    actualizar_producto,
    eliminar_producto,
    mostrar_inventario,
    buscar_producto
)"""
from ventas import registrar_venta
from reportes import generar_reportes

def main():
    inventario = cargar_inventario()

    while True:
        mostrar_menu()
        op = input("\nOpción: ").strip()

        match op:
            case "1":
                agregar_producto(inventario)
            case "2":
                actualizar_producto(inventario)
            case "3":
                eliminar_producto(inventario)
            case "4":
                mostrar_inventario(inventario)
            case "5":
                buscar_producto(inventario)
            case "6":
                registrar_venta(inventario)
            case "7":
                generar_reportes(inventario)
            case "8":
                print("Saliendo... Muchas gracias por usar Gifty.")
                break
            #el case nueve es opcional, se puede sar para que el usuario sepa donde se gusrda su df
            case "9":
                mostrar_ruta_excel()
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

