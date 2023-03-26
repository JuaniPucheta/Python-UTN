"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3 as sql

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """

    # Crear la conexion
    conexion = sql.connect("practica-04/ejercicio01.db")
    # Crear el cursor
    cursor = conexion.cursor()
    # Crear la tabla
    cursor.execute("CREATE TABLE Persona (IdPersona INTEGER PRIMARY KEY AUTOINCREMENT, Nombre CHAR(30), FechaNacimiento DATE, DNI INT, Altura INT)")
    # Guardar los cambios
    conexion.commit()
    # Cerrar la conexion
    conexion.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    # Crear la conexion
    conexion = sql.connect("practica-04/ejercicio01.db")
    # Crear el cursor
    cursor = conexion.cursor()
    # Borrar la tabla
    cursor.execute("DROP TABLE Persona")
    # Guardar los cambios
    conexion.commit()
    # Cerrar la conexion
    conexion.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN