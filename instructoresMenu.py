"""Menús de registro y consulta de instructores."""

from validaciones.entrada import pedir_documento, pedir_nombre_completo, pedir_opcion_con_numeros
from logica import instructores as logica
from interfaz.consola import despues_de_accion


def registrar_instructor():
    print("\n--- Registrar instructor ---")
    documento = pedir_documento()
    nombre = pedir_nombre_completo()
    print("\n¿Qué especialidad tiene?")
    print("  1. Moto  2. Carro  3. Ambos  4. Otro")
    especialidad = pedir_opcion_con_numeros("Seleccione (1/2/3/4 o escriba: moto/carro/ambos/otro): ",
                        logica.ESPECIALIDADES)
    ok, msg = logica.crear_instructor(documento, nombre, especialidad)
    print(msg if ok else f"Error: {msg}")
    despues_de_accion()


def consultar_instructores():
    print("\n--- Lista de instructores ---")
    lista = logica.listar_instructores()
    if not lista:
        print("No hay instructores registrados.")
    else:
        for i in lista:
            print(f"  {i['documento']} | {i['nombre']} | {i['especialidad']}")
    despues_de_accion()
