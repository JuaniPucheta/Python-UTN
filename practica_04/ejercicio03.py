"""Base de Datos SQL - Baja"""

import datetime

from ejercicio01 import reset_tabla, conn, cursor
from ejercicio02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""

    cursor.execute("SELECT * FROM persona WHERE id = ?", (id_persona,))
    persona = cursor.fetchone()
    if persona is None:
        return False
    else:
        cursor.execute("DELETE FROM persona WHERE id = ?", (id_persona,))
        conn.commit()          
    return True

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
