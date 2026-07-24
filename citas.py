"""Creación, consulta y disponibilidad de citas."""
from uuid import uuid4
from persistencia.jsonStore import cargar, guardar
from logica.agenda import ocupado, validar_momento
from logica.clientes import buscar_cliente
from logica.instructores import buscar_instructor
from logica.vehiculos import buscar_por_alias, vehiculos_por_tipo

ARCHIVO = "citas.json"


def _error_agenda(citas, cliente, instructor, vehiculo, fecha, hora, duracion):
    recursos = (("documento_cliente", cliente), ("documento_instructor", instructor), ("vehiculo", vehiculo))
    return next((f"{campo.replace('_', ' ')} ocupado en ese horario." for campo, valor in recursos if ocupado(citas, campo, valor, fecha, hora, duracion)), None)


def vehiculos_disponibles(tipo, fecha, hora, duracion):
    citas = cargar(ARCHIVO)
    return [vehiculo for vehiculo in vehiculos_por_tipo(tipo) if not ocupado(citas, "vehiculo", vehiculo["alias"], fecha, hora, duracion)]


def instructores_disponibles(tipo, fecha, hora, duracion):
    from logica.instructores import filtrar_por_especialidad
    citas = cargar(ARCHIVO)
    return [item for item in filtrar_por_especialidad(tipo) if not ocupado(citas, "documento_instructor", item["documento"], fecha, hora, duracion)]


def crear_cita(doc_cliente, doc_instructor, alias_vehiculo, fecha, hora, duracion):
    error = validar_momento(fecha, hora, duracion)
    cliente, instructor, vehiculo = buscar_cliente(doc_cliente), buscar_instructor(doc_instructor), buscar_por_alias(alias_vehiculo)
    if error or not cliente or not instructor or not vehiculo:
        return False, error or "Cliente, instructor o vehículo inexistente."
    if instructor["especialidad"] not in (vehiculo["tipo"], "ambos", "otro"):
        return False, "El instructor no coincide con el vehículo."
    citas = cargar(ARCHIVO)
    error = _error_agenda(citas, doc_cliente, doc_instructor, alias_vehiculo, fecha, hora, duracion)
    if error:
        return False, error
    citas.append({"id": uuid4().hex[:8], "documento_cliente": doc_cliente, "nombre_cliente": cliente["nombre"], "documento_instructor": doc_instructor, "nombre_instructor": instructor["nombre"], "vehiculo": alias_vehiculo, "fecha": fecha, "hora": hora, "duracion": duracion, "asistencia": None, "observacion": None})
    guardar(ARCHIVO, citas)
    return True, "Cita agendada correctamente."


def listar_citas():
    return cargar(ARCHIVO)


def filtrar_citas(documento=None, fecha=None):
    return [cita for cita in cargar(ARCHIVO) if (not documento or cita["documento_cliente"] == documento) and (not fecha or cita["fecha"] == fecha)]
