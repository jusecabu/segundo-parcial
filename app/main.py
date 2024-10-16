from hospital import Hospital
from persona_factory import PersonasFactory
from utils import mostrar_menu, int_input, continuar
from rich.prompt import Prompt
from rich.console import Console

hospital = Hospital()
OPCIONES_MENU_HOSPITAL = {
    1: "Buscar persona",
    2: "Agregar persona",
    3: "Menu paciente",
    4: "Menu medico",
    5: "Salir"
}
OPCIONES_MENU_PACIENTE = {
    1: "Talvez",
    2: "Atras"
}
OPCIONES_MENU_MEDICO = {
    1: "Talvez",
    2: "Atras"
}


while True:
    # print("\n--- Menú ---")
    # print("1. Agregar persona")
    # print("2. Pedir cita")
    # print("3. Cancelar cita")
    # print("4. Asignar médico de preferencia")
    # print("5. Ver citas pendientes")
    # print("6. Salir")

    opcion = mostrar_menu(OPCIONES_MENU_HOSPITAL, "MENU HOSPITAL")

    if opcion == 1:
        tipo_persona = Prompt.ask("Ingrese el tipo de persona", choices=["Medico", "Paciente"], case_sensitive=False).lower()
        identificacion = int_input("Ingrese la identificacion: ")

        if tipo_persona == "medico":
            persona = hospital.buscar_medico(identificacion)
        elif tipo_persona == "paciente":
            persona = hospital.buscar_paciente(identificacion)

        if persona != None:
            print(f"Se encontro el {tipo_persona}: {persona.nombre}")
        else:
            print(f"No se encontro el {tipo_persona}")

        continuar()
    elif opcion == 2:
        tipo_persona = Prompt.ask("Ingrese el tipo de persona", choices=["Medico", "Paciente"], case_sensitive=False).lower()
        identificacion = int_input("Ingrese la identificacion: ")
        nombre = input("Ingrese el nombre: ")
        celular = input("Ingrese el celular: ")

        if tipo_persona == "medico":
            especialidad = input("Ingrese la especialidad: ")
            persona = PersonasFactory.crear_persona(tipo_persona, identificacion, nombre, celular, especialidad)

            hospital.agregar_medico(persona)
        elif tipo_persona == "paciente":
            correo = input("Ingrese el correo: ")
            persona = PersonasFactory.crear_persona(tipo_persona, identificacion, nombre, celular, correo=correo)

            hospital.agregar_paciente(persona)
    elif opcion == 3:
        while True:
            opcion_paciente = mostrar_menu(OPCIONES_MENU_PACIENTE, "MENU PACIENTE")

            if opcion_paciente == 1:
                pass
            elif opcion_paciente == 2:
                break
        
    elif opcion == 4:
        while True:
            opcion_medico = mostrar_menu(OPCIONES_MENU_PACIENTE, "MENU MEDICO")

            if opcion_medico == 1:
                pass
            elif opcion_medico == 2:
                break

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    # elif opcion == 2:
    #     id_paciente = input("Ingrese la identificación del paciente: ")
    #     id_medico = input("Ingrese la identificación del médico: ")
    #     fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
    #     motivo = input("Ingrese el motivo de la cita: ")

    #     paciente = next(
    #         (p for p in hospital.usuarios if p.identificacion == id_paciente), None)
    #     medico = next(
    #         (m for m in hospital.medicos if m.identificacion == id_medico), None)

    #     if paciente and medico:
    #         paciente.pedir_cita(medico, fecha, motivo)
    #     else:
    #         print("Paciente o médico no encontrado.")

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

    # elif opcion == 4:
    #     id_paciente = int(input("Ingrese la identificación del paciente: "))
    #     id_medico = int(input("Ingrese la identificación del médico: "))

    #     paciente = next(
    #         (p for p in hospital.usuarios if p.identificacion == id_paciente), None)
    #     medico = next(
    #         (m for m in hospital.medicos if m.identificacion == id_medico), None)

    #     if paciente and medico:
    #         paciente.asignar_medico_preferencia(medico)
    #     else:
    #         print("Paciente o médico no encontrado.")

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

