El listado de los nuevos requerimientos que se pidieron.

- [ ] Corregir las Notificaciones
    - Los datos de correo, celular, etc. pertenecen a la Persona no a la Notificación.
    - El método enviar_notificación() debe ser heredado por todas las formas de notificación.
- [ ] Agregar Whatsapp como una forma de Notificación.
- [x] Corregir Agenda - Cita (la agenda no debe ir en el Paciente, o cada médico tiene una, o hay una general en el hospital)
- [x] Corregir Usuarios, no hay usuario, hay pacientes
- [x] Crear los métodos buscar_paciente() y buscar_medico() en el hospital
- [x] Corregir agendar y cancelar cita, no deben ir en el paciente sino donde tengan la agenda
- [ ] Cómo buscar los datos de una cita? en el Paciente, en el Hospital
- [ ] Revisar que hacer con "mover" citas 
- [x] Mejorar la interfaz de texto, utilizando la librería Rich: Menúes, Captura de Datos, Reportes.
- [ ] Cargar datos iniciales de Pacientes, Médicos y Citas, desde archivos CSV y JSON.
- [ ] Las Citas deben ir con Fecha y Hora (en intervalos de 20 minutos), no solo con la fecha.
- [ ] Al crear una nueva Cita, el Paciente selecciona la Especialidad y sistema muestra los Médicos con esa especialidad.