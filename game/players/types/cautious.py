# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Cautious Player Type Module.
"""
from game.players.types.bases import BasePlayerType


class Cautious(BasePlayerType):
    """
    Class to cautious player type.
    """

    def is_to_buy(self, prop):
        """
        Check if the player is to buy the property.
        :param prop: Property Object.
        :return: Boolean.
        """
        return super().is_to_buy(prop) and self._player.balance - prop.to_buy >= 80
