"""Lógica de negocio para vehículos."""
from persistencia.jsonStore import cargar, guardar
from logica.clientes import buscar_cliente

ARCHIVO = "vehiculos.json"
TIPOS_VEHICULO = ("moto", "carro", "otro")
PROPIETARIOS = ("publico", "cliente")


def _alias(tipo, vehiculos):
    return f"{tipo}{sum(item.get('tipo') == tipo for item in vehiculos) + 1}"


def crear_vehiculo(tipo, propietario, documento_cliente=None, placa=None):
    if tipo not in TIPOS_VEHICULO or propietario not in PROPIETARIOS:
        return False, "Tipo o propietario inválido.", None
    if propietario == "cliente" and not buscar_cliente(documento_cliente):
        return False, "No existe un cliente con ese documento.", None
    if not placa:
        return False, "La placa es obligatoria.", None
    vehiculos = cargar(ARCHIVO)
    if any(item.get("placa") == placa.upper() for item in vehiculos):
        return False, "Ya existe un vehículo con esa placa.", None
    alias = _alias(tipo, vehiculos)
    vehiculo = {"alias": alias, "placa": placa.upper(), "tipo": tipo, "propietario": propietario}
    if propietario == "cliente":
        vehiculo["documento_cliente"] = documento_cliente
    vehiculos.append(vehiculo)
    guardar(ARCHIVO, vehiculos)
    return True, f"Vehículo registrado como {alias}.", alias


def listar_vehiculos():
    return cargar(ARCHIVO)


def buscar_por_alias(alias):
    return next((item for item in cargar(ARCHIVO) if item.get("alias") == alias), None)


def vehiculos_por_tipo(tipo):
    return [item for item in cargar(ARCHIVO) if item.get("tipo") == tipo]
