"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3 as sql

from ejercicio01 import reset_tabla
from ejercicio02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    pass # Completar

    # Crear la conexion
    conexion = sql.connect("practica-04/ejercicio03.db")
    # Crear el cursor
    cursor = conexion.cursor()
    # Buscar la persona por su id y mostrarla por consola
    cursor.execute("SELECT * FROM Persona WHERE IdPersona = {}".format(id_persona))
    persona = cursor.fetchone()
    # Cerrar la conexion
    conexion.close()
    # Devolver la persona
    return persona
    

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN