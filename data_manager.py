import pandas as pd
import os

 
 
 
"""estas dos lineas ayuda que el archivo se cree y se guarde directamente
 en la carpeta GIFTYAPP, asi fucniona bien en cualquier pc"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_EXCEL = os.path.join(BASE_DIR, "data", "inventario_gifty_Grupo3.xlsx")

# cabeceras que ttendra nuestro df
COLUMNAS = ["COD", "NOMBRE", "PRECIO", "CANT", "VENDIDOS"]


 
"""funcion para mostar donde se guarda el archivo, 
se podria usar o saacar es opcional
 """ 
 
def mostrar_ruta_excel():
    """Muestra la ruta del archivo Excel que utiliza el sistema."""
    ruta = os.path.abspath(ARCHIVO_EXCEL)
    print("\n📍 Archivo Excel del inventario ubicado en:")
    print(ruta)


 
# funcion improtante que crea el archivo vacio la primera vez que corre el programa
 
def crear_archivo_excel_vacio():
    """
    Crea un archivo Excel vacío,si no existe,
    con las columnas oficiales del inventario.
    """
    if not os.path.exists(ARCHIVO_EXCEL):
        df_vacio = pd.DataFrame(columns=COLUMNAS)
        df_vacio.to_excel(ARCHIVO_EXCEL, index=False)
        print("\n🆕 Archivo Excel creado, la ruta la puede ver en la opcion 9.")
    else:
        print("\n✔ El archivo Excel ya existe. No fue necesario crearlo.")


 
# funcion para cargar inventario opcion4
 
def cargar_inventario():
    """
    Carga el inventario desde el archivo Excel.
    - Si el archivo no existe, lo crea vacío.
    - Retorna un diccionario de productos.

    Formato:
    inventario = {
        "p0001": {"nombre": "...", "precio": 2500, "cantidad": 50, "vendidos": 10},
        ...
    }
    """
    # Si no existe, se genera vacío
    if not os.path.exists(ARCHIVO_EXCEL):
        crear_archivo_excel_vacio()
        return {}

    df = pd.read_excel(ARCHIVO_EXCEL)

    inventario = {}

    for _, fila in df.iterrows():
        codigo = str(fila["COD"]).strip()

        inventario[codigo] = {
            "nombre": "" if pd.isna(fila.get("NOMBRE")) else str(fila["NOMBRE"]),
            "precio": 0.0 if pd.isna(fila.get("PRECIO")) else float(fila["PRECIO"]),
            "cantidad": 0 if pd.isna(fila.get("CANT")) else int(fila["CANT"]),
            "vendidos": 0 if pd.isna(fila.get("VENDIDOS")) else int(fila["VENDIDOS"]),
        }

    return inventario


 
# esta funcion guarda el inventario ene l excel
 
def guardar_inventario(inventario):
    """
    Recibe un diccionario con todos los productos
    y lo guarda en el archivo Excel .
    """
    lista_productos = []

    for codigo, datos in inventario.items():
        lista_productos.append({
            "COD": codigo,
            "NOMBRE": datos["nombre"],
            "PRECIO": datos["precio"],
            "CANT": datos["cantidad"],
            "VENDIDOS": datos["vendidos"],
        })

    df = pd.DataFrame(lista_productos, columns=COLUMNAS)
    df.to_excel(ARCHIVO_EXCEL, index=False)

    print("✔ Inventario guardado correctamente en Excel.")
