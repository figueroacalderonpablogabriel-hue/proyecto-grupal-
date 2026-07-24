"""Punto de entrada de la aplicación DriveSafe."""
from interfaz.consola import limpiar_pantalla, pausa
from menus.clientesMenu import consultar_clientes, registrar_cliente
from menus.citasMenu import consultar_citas, historial_cliente, programar_cita, registrar_asistencia
from menus.instructoresMenu import consultar_instructores, registrar_instructor
from menus.vehiculosMenu import consultar_vehiculos, registrar_vehiculo
from validaciones.entrada import pedir_opcion

OPCIONES = {"1": registrar_cliente, "2": consultar_clientes, "3": registrar_instructor, "4": consultar_instructores, "5": registrar_vehiculo, "6": consultar_vehiculos, "7": programar_cita, "8": consultar_citas, "9": registrar_asistencia, "10": historial_cliente}


def main():
    while True:
        limpiar_pantalla()
        print("""
--- DRIVE SAFE ---
1. Registrar cliente
2. Consultar clientes
3. Registrar instructor
4. Consultar instructores
5. Registrar vehículo
6. Consultar vehículos
7. Programar cita
8. Consultar citas
9. Registrar asistencia
10. Historial de cliente
0. Salir""")
        opcion = pedir_opcion("Seleccione una opción: ", tuple((*OPCIONES, "0")))
        if opcion == "0":
            return print("Saliendo...")
        accion = OPCIONES.get(opcion)
        if accion:
            limpiar_pantalla()
            accion()
        else:
            print("Opción inválida."); pausa()


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except KeyboardInterrupt:
            salir = pedir_opcion("\n¿Deseas salir? (si/no): ", ("si", "no"))
            if salir == "si":
                print("Saliendo de DriveSafe...")
                break
