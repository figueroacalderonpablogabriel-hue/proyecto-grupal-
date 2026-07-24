"""Asistencia e historial de citas."""
from persistencia.jsonStore import cargar, guardar

ARCHIVO = "citas.json"


def registrar_asistencia(identificador, asistio, observacion):
    citas = cargar(ARCHIVO)
    cita = next((item for item in citas if item.get("id") == identificador), None)
    if not cita:
        return False, "No existe una cita con ese identificador."
    cita["asistencia"] = "si" if asistio else "no"
    cita["observacion"] = observacion
    guardar(ARCHIVO, citas)
    return True, "Asistencia y observaciones registradas."


def historial_por_cliente(documento):
    return [cita for cita in cargar(ARCHIVO) if cita["documento_cliente"] == documento]
