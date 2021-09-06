# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Players Module.
"""
from enum import Enum

from src.core.settings import OPENING_BALANCE


class PlayerColor(Enum):
    """
    Class to define player color.
    """
    BLUE = 0, 'Blue'
    GREEN = 1, 'Green'
    YELLOW = 2, 'Yellow'
    RED = 3, 'Red'


class ClassicAliveRule:
    """
    Class to define alive rule.
    """

    def __init__(self, player):
        self._player = player

    def check(self):
        """
        Check if is alive.
        :return: Boolean.
        """
        return self._player.balance >= 0


class Player:
    """
    Class to Monopoly Player.
    """

    def __init__(self, color, player_type, balance=OPENING_BALANCE, alive_rule=ClassicAliveRule):
        self._balance = balance
        self._color = color
        self._is_alive = True
        self._player_type = player_type.new(self)
        self._alive_rule = alive_rule(self)

    def __str__(self):
        return f'[Player] Color: {self._color.value[1]}, Type: {self._player_type}, Balance: {self._balance}.'

    @property
    def player_type(self):
        """
        Get player type.
        :return: Object.
        """
        return self._player_type

    @property
    def color(self):
        """
        Get color value.
        :return: Player color value.
        """
        return self._color

    @property
    def balance(self):
        """
        Get balance value.
        :return: Float.
        """
        return self._balance

    @property
    def is_alive(self):
        """
        Check if player is alive.
        :return:  Boolean.
        """
        return self._alive_rule.check()

    def should_buy(self, prop):
        """
        Verify if player must buy the property.
        :return: Boolean.
        """
        return self._player_type.is_to_buy(prop)

    def buy(self, prop):
        """
        Method to buy a property.
        :param prop: Property Object.
        :return: Self.
        """
        if self._is_alive:
            self._balance -= prop.to_buy
            prop.owner = self
        return self

    def collect(self, value):
        """
        Method to receive a value from another player.
        :param value: Float.
        :return: Self.
        """
        if self._is_alive:
            self._balance += value
        return self

    def pay(self, value):
        """
        Method to pay a value from another player.
        :param value: Float.
        :return: Self.
        """
        if self._is_alive:
            self._balance -= value
        return self

    def receive_bonus(self, value):
        """
        Method to add value to balance.
        :param value: Float.
        :return: Self.
        """
        self._balance += value
        return self

    def pay_rent(self, prop, dice_value):
        """
        Method to pay rent for a property.
        :param prop: Property object.
        :param dice_value: Dice value to calculate rent value.
        :return: Self.
        """
        if self._is_alive:
            owner = prop.owner
            value = prop.to_rent(dice_value)
            self._balance -= value
            owner.receive_bonus(value)
        return self
