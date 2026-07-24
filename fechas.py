"""Entrada de fechas y horas con formato estricto."""
from datetime import date, datetime
from validaciones.entrada import _pedir


def fecha_valida(valor):
    try:
        return len(valor) == 10 and datetime.strptime(valor, "%Y-%m-%d").strftime("%Y-%m-%d") == valor
    except ValueError:
        return False


def hora_valida(valor):
    try:
        return len(valor) == 5 and datetime.strptime(valor, "%H:%M").strftime("%H:%M") == valor
    except ValueError:
        return False


def fecha_futura(valor):
    return fecha_valida(valor) and datetime.strptime(valor, "%Y-%m-%d").date() > date.today()


def pedir_fecha(mensaje):
    return _pedir(mensaje, fecha_valida, "Fecha inválida. Use AAAA-MM-DD.")


def pedir_fecha_futura(mensaje):
    return _pedir(mensaje, fecha_futura, "La fecha debe ser posterior a hoy.")


def pedir_hora(mensaje):
    return _pedir(mensaje, hora_valida, "Hora inválida. Use HH:MM.")
