"""Reglas reutilizables de disponibilidad por intervalos."""
from datetime import datetime
from validaciones.fechas import fecha_futura, hora_valida


def validar_momento(fecha, hora, duracion):
    if not fecha_futura(fecha) or not hora_valida(hora):
        return "La fecha debe ser futura y la hora válida."
    if not isinstance(duracion, int) or not 15 <= duracion <= 240:
        return "La duración debe estar entre 15 y 240 minutos."
    return None


def minutos(hora):
    tiempo = datetime.strptime(hora, "%H:%M")
    return tiempo.hour * 60 + tiempo.minute


def ocupado(citas, campo, valor, fecha, hora, duracion):
    inicio, fin = minutos(hora), minutos(hora) + duracion
    for cita in citas:
        if cita["fecha"] != fecha or cita.get(campo) != valor:
            continue
        otro_inicio = minutos(cita["hora"])
        if inicio < otro_inicio + cita["duracion"] and fin > otro_inicio:
            return True
    return False
