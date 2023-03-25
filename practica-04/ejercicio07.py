"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3 as sql

from ejercicio02 import agregar_persona
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
        with sql.connect('ejercicio06.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT IdPersona FROM Persona WHERE IdPersona = ?', (id_persona,))
            if cursor.fetchone() is None:
                return False
            cursor.execute(
                'SELECT IdPersona FROM PersonaPeso WHERE IdPersona = ? AND Fecha > ?', (id_persona, fecha))
            if cursor.fetchone() is not None:
                return False
            cursor.execute(
                'INSERT INTO PersonaPeso (IdPersona, Fecha, Peso) VALUES (?, ?, ?)', (id_persona, fecha, peso))
            conn.commit()
            return cursor.lastrowid
    except:
        return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
