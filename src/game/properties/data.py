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
    def get():
        """
        Get data.
        :return: Tuple.
        """
        return (
            Property('Av. 9 de julho', 30.0, 3.0),
            Property('Av. Brasil', 20.0, 1.5),
            Property('Av. Beira Mar', 15.0, 1.0),
            Property('Av. Rio Branco', 17.0, 1.2),
            Company('Companhia de Táxi', 23.0, 2),
            Property('Av. do Estado', 9.0, 0.5),
            Property('Av. do Contorno', 15.0, 1.1),
            Property('Av. Rebouças', 40.0, 7.0),
            Property('Av. Santo Amaro', 41.0, 7.2),
            Company('Companhia de Metrô', 25.0, 3),
            Property('Av. Juscelino Kubitschek', 14.0, 0.7),
            Property('Av. Morumbi', 22.0, 2.1),
            Property('Av. Higienópolis', 31.0, 2.9),
            Property('Av. São João', 41.0, 11.0),
            Company('Companhia Telefônica', 23.0, 2),
            Property('Av. Ipiranga', 33.0, 10.0),
            Property('Rua Brigadeiro Faria Lima', 30.5, 9.1),
            Property('Av. Paulista', 12.0, 1.3),
            Property('Av. Recife', 27.0, 1.9),
            Company('Companhia de Ônibus', 25.0, 3),
        )
