"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio01 import borrar_tabla, crear_tabla, conn, cursor

def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS personaPeso (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            idPersona INTEGER NOT NULL,
            fecha DATE, 
            peso INTEGER,
            FOREIGN KEY (idPersona) REFERENCES persona(id_persona)
            )'''
        )
        conn.commit()
        print('Tabla creada con exito')
        return True
    except:
        print('no se pudo crear la tabla')
        return False


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    try:
        cursor.execute('DROP TABLE IF EXISTS personaPeso')
        conn.commit()
        print('Tabla borrada con exito')
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
