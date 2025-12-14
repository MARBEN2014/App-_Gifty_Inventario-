from controlador import ejecutar_menu
from data_manager import cargar_inventario
from data_manager import cargar_inventario


def main():
    inventario = cargar_inventario()
    ejecutar_menu(inventario)


if __name__ == "__main__":
    main()

