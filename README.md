# Academia DriveSafe

Aplicación de consola para gestionar clientes, instructores, vehículos y citas de práctica en DriveSafe.

## Estructura simplificada

- [main.py](main.py): punto de entrada del programa.
- [menus/](menus): menús de consola por módulo.
- [logica/](logica): reglas de negocio y operaciones principales.
- [persistencia/](persistencia): carga y guardado en archivos JSON.
- [validaciones/](validaciones): validaciones de entrada y fechas.
- [interfaz/](interfaz): utilidades de consola.
- [data/](data): archivos JSON persistentes.

## Funcionalidades

- Registrar y consultar clientes.
- Registrar y consultar instructores.
- Registrar y consultar vehículos.
- Programar citas de práctica.
- Consultar citas por cliente o fecha.
- Registrar asistencia y observaciones.
- Consultar historial de prácticas por cliente.

## Uso

1. Ejecutar el programa:

```bash
python main.py
```

2. Elegir una opción del menú principal.
3. Complete los datos pedidos en consola.
4. Los registros se guardan automáticamente en la carpeta [data/](data).

## Archivos de datos

- [data/clientes.json](data/clientes.json)
- [data/instructores.json](data/instructores.json)
- [data/vehiculos.json](data/vehiculos.json)
- [data/citas.json](data/citas.json)

## Dependencias

Solo requiere Python 3 estándar.
