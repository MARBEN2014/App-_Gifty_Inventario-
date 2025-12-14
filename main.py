from controlador import ejecutar_menu
from data_manager import cargar_inventario, mostrar_ruta_excel
##from menu import mostrar_menu
##from crud import * 
##from ventas import registrar_venta
##from reportes import generar_reportes

def main():
    inventario = cargar_inventario()
    ejecutar_menu(inventario)


if __name__ == "__main__":
    main()

