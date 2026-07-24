"""Lógica de negocio para clientes."""
from persistencia.jsonStore import cargar
from logica.personas import buscar, crear

ARCHIVO = "clientes.json"
TIPOS_VEHICULO = ["carro", "moto", "ambos", "otro", "ningun vehiculo"]


def crear_cliente(documento, nombre, tipo_vehiculo):
    creado, mensaje = crear(ARCHIVO, documento, nombre, "tipo_vehiculo", tipo_vehiculo, TIPOS_VEHICULO)
    return creado, "Cliente registrado correctamente." if creado else mensaje


def listar_clientes():
    return cargar(ARCHIVO)


def buscar_cliente(documento):
    return buscar(ARCHIVO, documento)
