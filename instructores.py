"""Lógica de negocio para instructores."""
from persistencia.jsonStore import cargar
from logica.personas import buscar, crear

ARCHIVO = "instructores.json"
ESPECIALIDADES = ["moto", "carro", "ambos", "otro"]


def crear_instructor(documento, nombre, especialidad):
    creado, mensaje = crear(ARCHIVO, documento, nombre, "especialidad", especialidad, ESPECIALIDADES)
    return creado, "Instructor registrado correctamente." if creado else mensaje


def listar_instructores():
    return cargar(ARCHIVO)


def buscar_instructor(documento):
    return buscar(ARCHIVO, documento)


def filtrar_por_especialidad(tipo_vehiculo):
    return [item for item in cargar(ARCHIVO) if item["especialidad"] in (tipo_vehiculo, "ambos", "otro")]
