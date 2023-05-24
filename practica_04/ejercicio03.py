"""Base de Datos SQL - Baja"""

import datetime
import sqlite3 as sql

from ejercicio01 import reset_tabla
from ejercicio02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""

    conn = sql.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Persona WHERE IdPersona = ?", (id_persona,))

    conn.commit()
    conn.close()
    

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
