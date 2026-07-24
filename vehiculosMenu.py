"""Menú de vehículos."""
from interfaz.consola import despues_de_accion
from logica import vehiculos as logica
from validaciones.entrada import pedir_documento, pedir_opcion_con_numeros, pedir_placa


def registrar_vehiculo():
    print("\n--- Registrar vehículo ---")
    tipo = pedir_opcion_con_numeros("Tipo (1 moto, 2 carro, 3 otro): ", logica.TIPOS_VEHICULO)
    propietario = pedir_opcion_con_numeros("Propiedad (1 publico, 2 cliente): ", logica.PROPIETARIOS)
    documento = pedir_documento("Documento del propietario: ") if propietario == "cliente" else None
    ok, mensaje, _ = logica.crear_vehiculo(tipo, propietario, documento, pedir_placa())
    print(mensaje if ok else f"Error: {mensaje}")
    despues_de_accion()


def consultar_vehiculos():
    print("\n--- Lista de vehículos ---")
    for vehiculo in logica.listar_vehiculos():
        print(f"  {vehiculo['alias']} | {vehiculo.get('placa', 'sin placa')} | {vehiculo['tipo']} | {vehiculo['propietario']}")
    despues_de_accion()
