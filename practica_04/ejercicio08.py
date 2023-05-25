"""Base de datos SQL - Listar"""

import datetime

from ejercicio01 import conn, cursor
from ejercicio02 import agregar_persona
from ejercicio04 import buscar_persona
from ejercicio06 import reset_tabla
from ejercicio07 import agregar_peso


def listar_pesos(id_persona):
    """Implementar la funcion listar_pesos, que devuelva el historial de pesos 
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
     implementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente 
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """

    try: 
        #Primero valido que la persona exista
        if buscar_persona(id_persona) is None:
            print('La persona no existe')
            return False
        else:
            cursor.execute('SELECT fecha, peso FROM personaPeso WHERE idPersona = ?', (id_persona,))
            lista = cursor.fetchall()
            if lista is None:
                print('No se encontraron pesos')
                return False
            else: 
                # devuelvo la lista de pesos con el formato pedido
                return [(datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y-%m-%d'), peso) for fecha, peso in lista]
    except:
        print('No se pudo listar los pesos')
        return False



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
