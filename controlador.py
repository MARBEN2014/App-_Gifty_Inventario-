from menu import mostrar_menu
from crud import *
from ventas import registrar_venta
from reportes import generar_reportes
from data_manager import mostrar_ruta_excel


def ejecutar_menu(inventario):
    """
    Controla el flujo principal del programa.
    Contiene el loop del menú y las opciones disponibles.
    """

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
            case "9":
                mostrar_ruta_excel()
            case _:
                print("Opción inválida. Intente nuevamente.")
