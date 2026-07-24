"""Lectura y escritura JSON segura para la aplicación."""
import json
import os
import tempfile

CARPETA_DATOS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


class ErrorPersistencia(Exception):
    """Indica un archivo ilegible o un fallo al persistir datos."""


def _ruta(nombre_archivo):
    return os.path.join(CARPETA_DATOS, nombre_archivo)


def cargar(nombre_archivo):
    ruta = _ruta(nombre_archivo)
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except (OSError, json.JSONDecodeError) as error:
        raise ErrorPersistencia(f"No se pudo leer {nombre_archivo}.") from error
    if not isinstance(datos, list):
        raise ErrorPersistencia(f"{nombre_archivo} debe contener una lista JSON.")
    return datos


def guardar(nombre_archivo, datos):
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    ruta = _ruta(nombre_archivo)
    descriptor, temporal = tempfile.mkstemp(dir=CARPETA_DATOS, suffix=".tmp")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        os.replace(temporal, ruta)
    except OSError as error:
        if os.path.exists(temporal):
            os.unlink(temporal)
        raise ErrorPersistencia(f"No se pudo guardar {nombre_archivo}.") from error
