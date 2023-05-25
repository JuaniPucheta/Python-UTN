"""Base de Datos SQL - Baja"""

import datetime

from ejercicio01 import reset_tabla, sqlite3, conn, cursor
from ejercicio02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""

    try: 
        cursor.execute("DELETE FROM persona WHERE id_persona = ?", (id_persona,))
        conn.commit()    
        return True
    except Exception:
        print('Error al conectarse a la BD')
        return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    #! assert borrar_persona(12345) is False --> tira error

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
