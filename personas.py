"""Operaciones compartidas para clientes e instructores."""
from persistencia.jsonStore import cargar, guardar

ARCHIVOS_PERSONAS = ("clientes.json", "instructores.json")


def buscar(archivo, documento):
    return next((item for item in cargar(archivo) if item.get("documento") == documento), None)


def crear(archivo, documento, nombre, campo, valor, permitidos):
    if any(buscar(nombre_archivo, documento) for nombre_archivo in ARCHIVOS_PERSONAS):
        return False, "Ya existe un registro con ese documento."
    if valor not in permitidos:
        return False, f"{campo.capitalize()} inválido."
    registros = cargar(archivo)
    registros.append({"documento": documento, "nombre": nombre, campo: valor})
    guardar(archivo, registros)
    return True, "Registro creado correctamente."
