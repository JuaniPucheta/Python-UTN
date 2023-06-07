# Implementar los metodos de la capa de negocio de socios.
from practica_05.ejercicio02 import DatosSocio
from practica_05.ejercicio01 import Socio


class DniRepetido(Exception):
    Exception('El DNI ya esta registrado')

class LongitudInvalida(Exception):
    Exception('La longitud del nombre y/o apellido no es valida')

class MaximoAlcanzado(Exception):
    Exception('Se alcanzo el maximo de socios')

class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = self.datos.buscar(id_socio)
        if socio is None:
            print('No se encontro el socio')
            return None
        else:
            print('Socio encontrado: ', socio.nombre, socio.apellido, )
            return socio

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = self.datos.buscar(dni_socio)
        if socio is None:
            print('No se encontro el socio')
            return None
        else:
            print('Socio encontrado con dni: ', socio.dni)
            return socio

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios = self.datos.todos()
        if socios is None:
            print('No hay socios')
            return None
        else:
            print('Socios encontrados: ')
            for socio in socios:
                print(socio.nombre, socio.apellido, socio.dni)
            return socios
        
    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_1(socio) and self.regla_2(socio) and self.regla_3():
            self.datos.alta(socio)
            print('Socio dado de alta al validarse las 3 reglas')
            return True
        else: 
            print('No se pudo dar de alta al socio')
            return False
        

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        if self.datos.baja(id_socio):
            print('Socio dado de baja')
            return True
        else:
            print('No se pudo dar de baja al socio')
            return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio):
            self.datos.modificacion(socio)
            print('Socio modificado')
            return True
        else: 
            print('No se pudo modificar al socio')
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        if self.datos.buscar_dni(socio.dni):
            raise DniRepetido('El DNI ya esta registrado')
        else: 
            return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if len(socio.nombre) < self.MIN_CARACTERES or len(socio.nombre) > self.MAX_CARACTERES:
            print('Error regla 2, nombre')
            raise LongitudInvalida
        if len(socio.apellido) < self.MIN_CARACTERES or len(socio.apellido) > self.MAX_CARACTERES:
            print('Error regla 2, apellido')
            raise LongitudInvalida
        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos()) > self.MAX_SOCIOS:
            print('Error regla 3')
            raise MaximoAlcanzado
        else: 
            print('Pasa la regla 3')
            return True
