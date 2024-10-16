import os
from rich.table import Table
from rich.console import Console

def limpiar_consola():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

def mostrar_menu(opciones, nombre_menu):
    menu = Table(border_style="light_slate_grey")

    limpiar_consola()
    menu.add_column(nombre_menu, style="green", highlight=True, header_style="blue")

    for clave, valor in opciones.items():
        menu.add_row(f"{clave} {valor}")
    
    Console().print(menu)
    
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))

            if opcion in opciones:
                return opcion
            else:
                limpiar_consola()
                Console().print(menu)
                print(f"Opción no válida. Por favor, ingresa un número entre {min(opciones)} y {max(opciones)}.")
        except ValueError:
            limpiar_consola()
            Console().print(menu)
            print("Entrada inválida. Ingresa un número.")
            

def int_input(text, err_msg="Entrada inválida. Ingresa un número."):
    while True:
        try:
            opcion = int(input(text))

            return opcion
        except ValueError:
            print(err_msg)

def continuar():
    input("Presione cualquier tecla para continuar...")