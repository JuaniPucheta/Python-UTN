"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime

from ejercicio01 import conn, cursor
from ejercicio02 import agregar_persona
from ejercicio04 import buscar_persona
from ejercicio06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    try: 
        # Primero valido que la persona exista
        if buscar_persona(id_persona) is None:
            print('La persona no existe')
            return False
        else: 
            cursor.execute('SELECT * FROM personaPeso WHERE idPersona = ? AND fecha > ?', (id_persona, fecha))
            if cursor.fetchone() is not None:
                print('Ya existe un registro de fecha posterior')
                return False
            else:
                cursor.execute(
                    'INSERT INTO personaPeso (idPersona, fecha, peso) VALUES (?, ?, ?)', (id_persona, fecha, peso)
                )
                conn.commit()
                return cursor.lastrowid
    except:
        print('No se pudo agregar el peso')
        return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
