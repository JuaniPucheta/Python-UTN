"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS persona (
            id_persona INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT, 
            fechaNacimiento DATE, 
            dni INTEGER, 
            altura INTEGER
        )'''
    )
    print('Tabla creada con exito')
    conn.commit()

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    cursor.execute("DROP TABLE persona")

    conn.commit()

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

crear_tabla()