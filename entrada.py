"""Validaciones reutilizables para entradas de consola."""
import re



def _pedir(mensaje, valida, error):
    while True:
        valor = input(mensaje).strip()
        if valida(valor):
            return valor
        print(f"  {error}")




def pedir_texto(mensaje):
    return _pedir(mensaje, bool, "Este campo no puede estar vacío.")






def pedir_documento(mensaje="Documento (solo números): "):
    return _pedir(mensaje, str.isdigit, "El documento solo puede contener números.")


def pedir_nombre_completo(mensaje="Nombre completo: "):
    return _pedir(mensaje, lambda valor: len(valor) >= 6, "El nombre debe tener al menos 6 caracteres.")


def pedir_placa(mensaje="Placa: "):
    patron = re.compile(r"^[A-Za-z0-9-]{5,8}$")
    return _pedir(mensaje, lambda valor: bool(patron.fullmatch(valor)), "La placa debe tener 5 a 8 caracteres alfanuméricos.").upper()


def pedir_entero(mensaje, minimo=None, maximo=None):
    def valido(valor):
        return valor.isdigit() and (minimo is None or int(valor) >= minimo) and (maximo is None or int(valor) <= maximo)
    return int(_pedir(mensaje, valido, f"Ingrese un número entre {minimo} y {maximo}."))


def pedir_opcion(mensaje, opciones):
    opciones = [opcion.lower() for opcion in opciones]
    return _pedir(mensaje, lambda valor: valor.lower() in opciones, f"Opción válida: {', '.join(opciones)}.").lower()


def pedir_opcion_con_numeros(mensaje, opciones):
    opciones = [opcion.lower() for opcion in opciones]
    valor = _pedir(mensaje, lambda valor: valor.lower() in opciones or valor.isdigit() and 1 <= int(valor) <= len(opciones), "Opción inválida.").lower()
    return opciones[int(valor) - 1] if valor.isdigit() else valor
