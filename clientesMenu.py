"""Menús de registro y consulta de clientes."""

from validaciones.entrada import  pedir_documento, pedir_nombre_completo, pedir_opcion_con_numeros
from logica import clientes as logica
from interfaz.consola import despues_de_accion


def registrar_cliente():
    print("\n--- Registrar cliente ---")
    documento = pedir_documento()
    
    nombre = pedir_nombre_completo()

    print("\n¿Tiene vehículo?")
    print("  1. Carro  2. Moto  3. Ambos  4. Otro  5. Ningún vehículo")

    tipo = pedir_opcion_con_numeros(
        "Seleccione (1/2/3/4/5 o escriba: carro/moto/ambos/otro/ningun vehiculo): ",
        logica.TIPOS_VEHICULO
    )

    ok, msg = logica.crear_cliente(documento, nombre, tipo)
    print(msg if ok else f"Error: {msg}")
    despues_de_accion()

def consultar_clientes():
    print("\n--- Lista de clientes ---")
    lista = logica.listar_clientes()
    if not lista:
        print("No hay clientes registrados.")
    else:
        for c in lista:
            print(f"  {c['documento']} | {c['nombre']} | {c['tipo_vehiculo']}")
    despues_de_accion()



    