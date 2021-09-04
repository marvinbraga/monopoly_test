# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Monopoly Abstract Properties Module.
"""
from abc import ABCMeta, abstractmethod


class AbstractProperty(metaclass=ABCMeta):
    """
    Abstract class to Property.
    """

    def __init__(self, name, to_buy, to_rent):
        self._name = name
        self._to_rent = to_rent
        self._to_buy = to_buy
        self._owner = None

    def __str__(self):
        return f'[{self.__class__.__name__}] Name: {self._name}, Owner: {self._owner}, ' \
               f'Rent: {self._to_rent}, Buy: {self._to_buy}.'

    @property
    def owner(self):
        """
        Get the Owner's property value.
        :return: Player object.
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Set the Owner's property value.
        :param value: Player object.
        :return: Self.
        """
        self._owner = value

    @abstractmethod
    def to_rent(self, dice_value=0):
        """
        Method to calculate the rent value.
        :return: Float.
        """
        pass

    @property
    def to_buy(self):
        """
        Method to calculate the buy value.
        :return: Float.
        """
        return self._to_buy
