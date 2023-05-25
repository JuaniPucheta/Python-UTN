"""Base de Datos SQL - Búsqueda"""

import datetime

from ejercicio01 import reset_tabla, cursor
from ejercicio02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    pass 

    try:
        cursor.execute("SELECT * FROM persona WHERE id_persona = ?", (id_persona,))
        persona = cursor.fetchone()
        if persona is None:
            return False
        else: 
            return persona
    except Exception:
        print('Error al conectarse a la BD')
    
    
# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN