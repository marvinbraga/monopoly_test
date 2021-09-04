# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Base Player Type Module.
"""


class BasePlayerType:
    """
    Class to base player types.
    """
    def __init__(self, player):
        self._player = player

    def is_to_buy(self, prop):
        """
        Check if the player is to buy the property.
        :param prop: Property Object.
        :return: Boolean.
        """
        return self._player.is_alive and self._player.balance > 0
