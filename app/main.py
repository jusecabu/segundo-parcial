from hospital import Hospital
from persona_factory import PersonasFactory
from cita import Cita
from utils import mostrar_menu, int_input, continuar
from rich.prompt import Prompt
import csv
import json

# Crear el hospital y los menus de la aplicacion
hospital = Hospital()
OPCIONES_MENU_HOSPITAL = {
    1: "Buscar persona",
    2: "Agregar persona",
    3: "Menu paciente",
    4: "Menu medico",
    5: "Salir",
}
OPCIONES_MENU_PACIENTE = {
    1: "Pedir cita",
    2: "Cancelar cita",
    3: "Mover cita - WP",
    4: "Asignar medico de preferencia",
    5: "Atras",
}
OPCIONES_MENU_MEDICO = {1: "WP", 2: "Atras"}

# Cargar los datos de medicos y pacientes
medicos_data = []
pacientes_data = []

with open("./data/medicos.json", encoding="utf-8") as medicos_json:
    medicos_data = json.load(medicos_json)

with open("./data/pacientes.csv", encoding="utf-8") as pacientes_csv:
    fuente = csv.reader(pacientes_csv, delimiter=",")

    for linea in fuente:
        pacientes_data.append(linea)

del pacientes_data[0]

for medico_data in medicos_data:
    persona = PersonasFactory.crear_persona(
        "medico",
        int(medico_data["id"]),
        medico_data["nombre"],
        medico_data["celular"],
        medico_data["especialidad"],
    )

    hospital.agregar_medico(persona)

for paciente_data in pacientes_data:
    persona = PersonasFactory.crear_persona(
        "paciente",
        int(paciente_data[0]),
        paciente_data[1],
        paciente_data[2],
        correo=paciente_data[3],
    )

    hospital.agregar_paciente(persona)

# Aplicacion
while True:
    opcion = mostrar_menu(OPCIONES_MENU_HOSPITAL, "Menu hospital")

    if opcion == 1:
        tipo_persona = Prompt.ask(
            "Ingrese el tipo de persona",
            choices=["Medico", "Paciente"],
            case_sensitive=False,
        ).lower()
        identificacion = int_input("Ingrese la identificacion: ")

        if tipo_persona == "medico":
            persona = hospital.buscar_medico(identificacion)
        elif tipo_persona == "paciente":
            persona = hospital.buscar_paciente(identificacion)

        if persona is not None:
            print(f"Se encontro el {tipo_persona} {persona.nombre}")
        else:
            print(f"No se encontro el {tipo_persona}")

        continuar()

    elif opcion == 2:
        tipo_persona = Prompt.ask(
            "Ingrese el tipo de persona",
            choices=["Medico", "Paciente"],
            case_sensitive=False,
        ).lower()
        identificacion = int_input("Ingrese la identificacion: ")
        nombre = input("Ingrese el nombre: ")
        celular = input("Ingrese el celular: ")

        if tipo_persona == "medico":
            especialidad = input("Ingrese la especialidad: ")
            persona = PersonasFactory.crear_persona(
                tipo_persona, identificacion, nombre, celular, especialidad
            )

            hospital.agregar_medico(persona)
        elif tipo_persona == "paciente":
            correo = input("Ingrese el correo: ")
            persona = PersonasFactory.crear_persona(
                tipo_persona, identificacion, nombre, celular, correo=correo
            )

            hospital.agregar_paciente(persona)

    elif opcion == 3:
        identificacion = int_input("Ingrese la identificacion: ")
        paciente = hospital.buscar_paciente(identificacion)

        if paciente is not None:
            while True:
                opcion_paciente = mostrar_menu(
                    OPCIONES_MENU_PACIENTE, f"Menu paciente | {paciente.nombre}"
                )

                if opcion_paciente == 1:
                    while True:
                        identificacion_med = input(
                            "Ingrese la identificacion (En blanco para medico de preferencia): "
                        )

                        if identificacion_med == "":
                            medico = paciente.medico_preferencia

                            if medico is not None:
                                break
                            else:
                                print("No tiene un medico de preferencia")
                        elif identificacion_med == "salir":
                            break
                        else:
                            try:
                                identificacion_med = int(identificacion_med)

                                medico = hospital.buscar_medico(identificacion_med)

                                if medico is not None:
                                    break
                                else:
                                    print("No se encontro el medico")
                            except ValueError:
                                print("Entrada inválida. Ingresa un número.")

                    if medico is not None:
                        fecha = input(
                            "Ingrese la fecha de la cita (YYYY-MM-DD/HH:MM): "
                        )
                        cita = Cita(paciente, medico, fecha)

                        if medico.verificar_disponibilidad(fecha):
                            medico.agenda.agregar_cita(cita)
                        else:
                            print("El medico no tiene disponibilidad")

                        continuar()

                elif opcion_paciente == 2:
                    pass

                elif opcion_paciente == 4:
                    identificacion_med = int_input("Ingrese la identificacion: ")
                    medico = hospital.buscar_medico(identificacion_med)

                    if medico is not None:
                        paciente.asignar_medico_preferencia(medico)
                    else:
                        print("No se encontro el medico")

                    continuar()
                elif opcion_paciente == 5:
                    break
        else:
            print("No se encontro el paciente")
            continuar()
    elif opcion == 4:
        while True:
            opcion_medico = mostrar_menu(OPCIONES_MENU_MEDICO, "Menu medico")

            if opcion_medico == 1:
                print("Trabajando en ello")
                pass
            elif opcion_medico == 2:
                break

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    # elif opcion == 3:
    #     id_paciente = int(input("Ingrese la identificación del paciente: "))
    #     paciente = next(
    #         (p for p in hospital.usuarios if p.identificacion == id_paciente), None)

    #     if paciente:
    #         print("Citas pendientes:")
    #         for i, cita in enumerate(paciente.agenda.citas_pendientes):
    #             print(f"{i+1}. {cita}")

    #         opcion_cita = int(input("Seleccione la cita a cancelar: "))
    #         if 1 <= opcion_cita <= len(paciente.agenda.citas_pendientes):
    #             cita_a_cancelar = paciente.agenda.citas_pendientes[opcion_cita - 1]
    #             paciente.cancelar_cita(cita_a_cancelar)
    #         else:
    #             print("Opción inválida.")
    #     else:
    #         print("Paciente no encontrado.")

    # elif opcion == 5:
    #     id_paciente = int(input("Ingrese la identificación del paciente: "))
    #     paciente = next(
    #         (p for p in hospital.usuarios if p.identificacion == id_paciente), None)

    #     if paciente:
    #         print("Citas pendientes:")
    #         for cita in paciente.agenda.citas_pendientes:
    #             print(cita)
    #     else:
    #         print("Paciente no encontrado.")
