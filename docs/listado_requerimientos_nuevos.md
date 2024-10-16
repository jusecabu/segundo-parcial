El listado de los nuevos requerimientos que se pidieron.

1. Corregir las Notificaciones
    - Los datos de correo, celular, etc. pertenecen a la Persona no a la Notificación.
    - El método enviar_notificación() debe ser heredado por todas las formas de notificación.
2. Agregar Whatsapp como una forma de Notificación.
3. Corregir Agenda - Cita (la agenda no debe ir en el Paciente, o cada médico tiene una, o hay una general en el hospital)
4. Corregir Usuarios, no hay usuario, hay pacientes
5. Crear los métodos buscar_paciente() y buscar_medico() en el hospital
6. Corregir agendar y cancelar cita, no deben ir en el paciente sino donde tengan la agenda
7. Cómo buscar los datos de una cita? en el Paciente, en el Hospital
8. Revisar que hacer con "mover" citas 
9. Mejorar la interfaz de texto, utilizando la librería Rich: Menúes, Captura de Datos, Reportes.
10. Cargar datos iniciales de Pacientes, Médicos y Citas, desde archivos CSV y JSON.
11. Las Citas deben ir con Fecha y Hora (en intervalos de 20 minutos), no solo con la fecha.
12. Al crear una nueva Cita, el Paciente selecciona la Especialidad y sistema muestra los Médicos con esa especialidad.