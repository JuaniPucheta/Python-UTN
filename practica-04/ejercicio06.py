"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio01 import borrar_tabla, crear_tabla
import sqlite3 as sql


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    try:
        with sql.connect('ejercicio06.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS PersonaPeso (IdPersona INTEGER, Fecha DATE, Peso INTEGER)')
            conn.commit()
            return True
    except:
        return False


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    try:
        with sql.connect('ejercicio06.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE PersonaPeso')
            conn.commit()
            return True
    except:
        return False


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
