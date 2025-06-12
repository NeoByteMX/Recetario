"""
Modulso requeridos para manejar las librearias
"""
from pathlib import Path
import os


def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system("cls")

def saludo():
    print("¡Bienvenido al recetario!\n")


def menu_opciones():
    """Despluega el menú de opciones, la opción es una str"""
    print("----- Menú Principal ------")
    print("Por favor selecciona una opción:")
    print("""
    [1] Leer receta
    [2] Crear receta
    [3] Crear categoría
    [4] Eliminar receta
    [5] Eliminar categoría
    [6] Finalizar programa""")
    opcion = input()
    return opcion

def eliminar_receta():
    """
    Selecciona una receta para eliminarla
    """
    ruta, receta = elegir_receta() #Valida la ruta y el nombre del archivo de la receta
    mi_archivo = Path(ruta)/receta # Crea la ruta absoluta del archivo
    # Valida si quiere eliminar el archivo
    eliminar = input(f"¿Seguro que quieres eliminar {mi_archivo}?\n S/N:")
    if eliminar.upper() == "S":
        print(f"¡Se ha eliminado con exito {mi_archivo}!")
        os.remove(mi_archivo) #Elimina el archivo
    else:
        print(f"¡No se ha eliminado la receta {mi_archivo}!")

def leer_receta():
    """ Lee la receta"""
    while True:
        ruta, receta = elegir_receta()
        mi_archivo = Path(ruta)/receta
        if mi_archivo.exists():
            limpiar_pantalla()
            print(mi_archivo.read_text())
            input()
            limpiar_pantalla()
            break
        else:
            print("No existe esa receta")
            volver = input("¿Quieres seleccionar otra receta?\nS/N: ")
            if volver.upper() == "N":
                break


def elegir_categoria():
    ruta_recetario = Path("Recetas")
    while True:
        print("Elige la categoría: ")
        for carpeta in ruta_recetario.iterdir():
            print(carpeta.name)
        categoria = input()
        for carpeta in ruta_recetario.iterdir():
            if categoria in carpeta.name:
                return Path(ruta_recetario, categoria)
        limpiar_pantalla()
        print("Esa categoría no existe, selecciona otra\n")


def elegir_receta():
    ruta = elegir_categoria()
    limpiar_pantalla()
    print("Elige la receta: ")
    for file in ruta.iterdir():
        print(file.name)
    receta = input() + ".txt"
    return ruta, receta

def crear_receta():
    contenido = input("¿Cuál es la receta?\n")
    directorio = elegir_categoria()
    nombre_receta = input("¿Cómo se va a allamar la receta?\n ") + ".txt"
    for receta in directorio.iterdir():
        if nombre_receta == receta.name:
            print("Ya existe esa receta")
            nombre_receta = input("¿Cómo se va a allamar la receta?\n ") + ".txt"
        else:
            file = open(directorio/nombre_receta, "w")
            file.write(contenido)
            file.close()
            print(f"¡Se ha creado exitosamente {nombre_receta}!")
            input()
            limpiar_pantalla()
            break

def crear_categoria():
    while True:
        categoria = input("¿Cuál es el nombre de la categoría?\n")
        ruta = Path("Recetas")
        nueva_categoria = ruta / categoria
        if nueva_categoria in ruta.iterdir():
            print("Ya existe esa categoría\n")
            crear = input("¿Deseas crear una nueva categoría?\nS/N: ")
            if crear.upper() == "N" or crear.upper() == "No":
                print("¡No se ha creado ninguna categoría!")
        else:
            validacion = input(f"¿Es correcto el nombre de la categoria?: \"{categoria}\" \nS/N: ")
            if validacion.upper() == "S" or validacion.upper() == "Si":
                os.mkdir(ruta / categoria)
                print(f"¡La categoría {categoria} se ha creado con exito!")
                input()
                limpiar_pantalla()
                break
            crear = input("¿Deseas crear una nueva categoría?\nS/N: ")
            if crear.upper() == "N" or crear.upper() == "No":
                limpiar_pantalla()
                return None

def eliminar_categoria():
    while True:
        print("¿Qué categoría desea elminar?\n")
        for carpeta in Path("Recetas").iterdir():
            print(carpeta.name)
        categoria = input()
        ruta = Path("Recetas")
        categoria_eliminar = ruta / categoria
        if categoria_eliminar not in ruta.iterdir():
            limpiar_pantalla()
            print("No esiste esa categoría\n")
            eliminar = input("¿Deseas eliminar una categoría?\nS/N: ")
            if eliminar.upper() == "N" or eliminar.upper() == "No":
                print("¡No se ha eliminado ninguna categoría!")
                eliminar_categoria = input("¿Deseas eliminar una categoría?\nS/N: ")
                if eliminar_categoria.upper() == "N" or eliminar_categoria.upper() == "No":
                    return None
        else:
            validacion = input(f"¿Es correcto el nombre de la categoria?: \"{categoria}\" \nS/N: ")
            if validacion.upper() == "S" or validacion.upper() == "Si":
                for file in categoria_eliminar.iterdir():
                    os.remove(file)
                os.removedirs(categoria_eliminar)
                limpiar_pantalla()
                print(f"¡La categoría {categoria} se ha eliminado con exito!")
                input()
                limpiar_pantalla()
                break

def recetario():
    seleccion = 0
    saludo()
    while seleccion != "6":
        seleccion = menu_opciones()
        if seleccion == "1":
            limpiar_pantalla()
            leer_receta()
        elif seleccion == "2":
            limpiar_pantalla()
            crear_receta()
        elif seleccion == "3":
            limpiar_pantalla()
            crear_categoria()
        elif seleccion == "4":
            limpiar_pantalla()
            eliminar_receta()
        elif seleccion == "5":
            limpiar_pantalla()
            eliminar_categoria()

if __name__ == "__main__":
    recetario()