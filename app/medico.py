from persona import Persona
from agenda import Agenda


class Medico(Persona):
    def __init__(self, identificacion, nombre, celular, especialidad):
        super().__init__(identificacion, nombre, celular)
        self.especialidad = especialidad
        self.agenda = Agenda()

    def verificar_disponibilidad(self, fecha):
        # Verifica si tiene citas pendientes en la fecha dada
        for cita in self.agenda.citas_pendientes:
            if fecha == cita.fecha:
                return False

        return True
