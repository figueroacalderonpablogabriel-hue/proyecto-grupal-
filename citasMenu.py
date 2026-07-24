"""Menú de programación, consulta e historial de citas."""
from interfaz.consola import despues_de_accion
from logica import asistencia, citas, clientes
from validaciones.entrada import pedir_documento, pedir_entero, pedir_opcion, pedir_opcion_con_numeros, pedir_texto
from validaciones.fechas import pedir_fecha, pedir_fecha_futura, pedir_hora

TIPOS_VEHICULO = ("carro", "moto", "otro")


def _seleccionar(registros, etiqueta, campo="documento"):
    for indice, registro in enumerate(registros, 1):
        if "nombre_cliente" in registro:
            print(f"  {indice}. {registro['nombre_cliente']} | {registro['fecha']} {registro['hora']} | {registro['vehiculo']}")
        elif "placa" in registro:
            print(f"  {indice}. {registro['alias']} | placa: {registro['placa']}")
        else:
            print(f"  {indice}. {registro['nombre']} ({registro[campo]})")
    while True:
        valor = input(f"Seleccione {etiqueta}: ").strip()
        if valor.isdigit() and 1 <= int(valor) <= len(registros):
            return registros[int(valor) - 1]
        encontrado = next((item for item in registros if item[campo] == valor), None)
        if encontrado:
            return encontrado
        print("  Selección inválida.")


def _imprimir(cita):
    print(f"  ID {cita.get('id', 'sin-id')} | {cita['fecha']} {cita['hora']} | {cita['duracion']} min")
    print(f"  Cliente: {cita['nombre_cliente']} | Instructor: {cita['nombre_instructor']} | Vehículo: {cita['vehiculo']}")
    print(f"  Asistencia: {cita.get('asistencia') or 'pendiente'} | Observación: {cita.get('observacion') or '-'}")


def programar_cita():
    print("\n--- Programar cita ---")
    lista_clientes = clientes.listar_clientes()
    if not lista_clientes:
        print("Error: primero registre un cliente."); despues_de_accion(); return
    cliente = _seleccionar(lista_clientes, "cliente")
    tipo = pedir_opcion_con_numeros("Tipo (1 carro, 2 moto, 3 otro): ", TIPOS_VEHICULO)
    fecha, hora = pedir_fecha_futura("Fecha futura (AAAA-MM-DD): "), pedir_hora("Hora (HH:MM): ")
    duracion = pedir_entero("Duración (15-240 min): ", 15, 240)
    instructores = citas.instructores_disponibles(tipo, fecha, hora, duracion)
    vehiculos = citas.vehiculos_disponibles(tipo, fecha, hora, duracion)
    if not instructores or not vehiculos:
        print("No hay instructor o vehículo disponible para ese horario."); despues_de_accion(); return
    instructor = _seleccionar(instructores, "instructor")
    vehiculo = _seleccionar(vehiculos, "vehículo", "alias")
    ok, mensaje = citas.crear_cita(cliente["documento"], instructor["documento"], vehiculo["alias"], fecha, hora, duracion)
    print(mensaje if ok else f"Error: {mensaje}")
    despues_de_accion()


def consultar_citas():
    opcion = pedir_opcion("Consultar: 1 todas, 2 cliente, 3 fecha: ", ("1", "2", "3"))
    documento = pedir_documento() if opcion == "2" else None
    fecha = pedir_fecha("Fecha: ") if opcion == "3" else None
    resultado = citas.filtrar_citas(documento, fecha)
    print("No se encontraron citas." if not resultado else f"\n--- {len(resultado)} citas ---")
    for cita in resultado:
        _imprimir(cita)
    despues_de_accion()


def registrar_asistencia():
    pendientes = [cita for cita in citas.listar_citas() if cita.get("asistencia") is None]
    if not pendientes:
        print("No hay citas pendientes de asistencia."); despues_de_accion(); return
    print("\n--- Seleccione la cita ---")
    identificador = _seleccionar(pendientes, "cita", "id")["id"]
    asistio = pedir_opcion("¿Asistió? (si/no): ", ("si", "no")) == "si"
    ok, mensaje = asistencia.registrar_asistencia(identificador, asistio, pedir_texto("Observación: "))
    print(mensaje if ok else f"Error: {mensaje}")
    despues_de_accion()


def historial_cliente():
    resultado = asistencia.historial_por_cliente(pedir_documento())
    print("Sin prácticas registradas." if not resultado else f"\n--- Historial ({len(resultado)}) ---")
    for cita in resultado:
        _imprimir(cita)
    despues_de_accion()
