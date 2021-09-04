# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Dices Module.
"""
from random import randint


class Dice:
    """
    Class to simulate a dice.
    """

    def __init__(self, value=1):
        self._value = value

    @property
    def roll(self):
        """
        Perform the dice roll.
        :return: Dice value.
        """
        self._value = randint(1, 6)
        return self._value
