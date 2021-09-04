# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Monopoly Properties Module.
"""
from game.properties.abstracts import AbstractProperty


class Property(AbstractProperty):
    """
    Abstract class to Property.
    """

    def to_rent(self, dice_value=0):
        """
        Method to calculate the rent value.
        :param dice_value: Int.
        :return: Float.
        """
        _ = dice_value
        return self._to_rent


class Company(AbstractProperty):
    """
    Abstract class to Property.
    """

    def to_rent(self, dice_value=0):
        """
        Method to calculate the rent value.
        :param dice_value: Int.
        :return: Float.
        """
        return self._to_rent * dice_value
