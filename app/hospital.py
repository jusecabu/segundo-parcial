class Hospital:
    __instance = None

    def get_instance(self):
        if Hospital.__instance is None:
            Hospital()
        return Hospital.__instance

    def __init__(self):
        self.pacientes = []
        self.medicos = []

    def buscar_paciente(self, identificacion):
        for paciente in self.pacientes:
            if paciente.identificacion == identificacion:
                return paciente

    def buscar_medico(self, identificacion):
        for medico in self.medicos:
            if medico.identificacion == identificacion:
                return medico

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nombre} agregado al hospital.")

    def agregar_medico(self, medico):
        self.medicos.append(medico)
        print(f"Médico {medico.nombre} agregado al hospital.")

    # def verificar_disponibilidad(self, paciente, especialidad):
    #     for medico in self.medicos:
    #         if medico.especialidad == especialidad:
    #             if medico.verificar_disponibilidad(paciente.agenda.fecha):
    #                 return medico
    #     print(
    #         f"No se encontró disponibilidad para la especialidad {especialidad}.")
