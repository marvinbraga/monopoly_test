# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Properties Data Module.
"""
from src.game.properties.classes import Property, Company


class PropertyData:
    """
    Class to define the properties data.
    """
    @staticmethod
    def _value_upgrade(value, factor=3):
        return value * factor

    @staticmethod
    def _rent_upgrade(value, factor=7):
        return value * factor

    @staticmethod
    def get():
        """
        Get data.
        :return: Tuple.
        """
        return [
            Property('Av. 9 de julho', PropertyData._value_upgrade(30.0), PropertyData._rent_upgrade(3.0)),
            Property('Av. Brasil', PropertyData._value_upgrade(20.0), PropertyData._rent_upgrade(1.5)),
            Property('Av. Beira Mar', PropertyData._value_upgrade(15.0), PropertyData._rent_upgrade(1.0)),
            Property('Av. Rio Branco', PropertyData._value_upgrade(17.0), PropertyData._rent_upgrade(1.2)),
            Company('Companhia de Táxi', PropertyData._value_upgrade(23.0), PropertyData._rent_upgrade(0.2)),
            Property('Av. do Estado', PropertyData._value_upgrade(9.0), PropertyData._rent_upgrade(0.5)),
            Property('Av. do Contorno', PropertyData._value_upgrade(15.0), PropertyData._rent_upgrade(1.1)),
            Property('Av. Rebouças', PropertyData._value_upgrade(40.0), PropertyData._rent_upgrade(7.0)),
            Property('Av. Santo Amaro', PropertyData._value_upgrade(41.0), PropertyData._rent_upgrade(7.2)),
            Company('Companhia de Metrô', PropertyData._value_upgrade(25.0), PropertyData._rent_upgrade(2.5)),
            Property('Av. Juscelino Kubitschek', PropertyData._value_upgrade(14.0), PropertyData._rent_upgrade(0.7)),
            Property('Av. Morumbi', PropertyData._value_upgrade(22.0), PropertyData._rent_upgrade(2.1)),
            Property('Av. Higienópolis', PropertyData._value_upgrade(31.0), PropertyData._rent_upgrade(2.9)),
            Property('Av. São João', PropertyData._value_upgrade(41.0), PropertyData._rent_upgrade(11.)),
            Company('Companhia Telefônica', PropertyData._value_upgrade(23.0), PropertyData._rent_upgrade(2.2)),
            Property('Av. Ipiranga', PropertyData._value_upgrade(33.0), PropertyData._rent_upgrade(7.0)),
            Property('Rua Brigadeiro Faria Lima', PropertyData._value_upgrade(30.5), PropertyData._rent_upgrade(9.1)),
            Property('Av. Paulista', PropertyData._value_upgrade(12.0), PropertyData._rent_upgrade(1.3)),
            Property('Av. Recife', PropertyData._value_upgrade(27.0), PropertyData._rent_upgrade(1.9)),
            Company('Companhia de Ônibus', PropertyData._value_upgrade(25.0), PropertyData._rent_upgrade(3.2)),
        ]
