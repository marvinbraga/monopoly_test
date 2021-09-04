# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Impulsive Player Type Module.
"""
from src.game.players.types.bases import BasePlayerType


class Demanding(BasePlayerType):
    """
    Class to demanding player type.
    """

    def is_to_buy(self, prop):
        """
        Check if the player is to buy the property.
        :param prop: Property Object.
        :return: Boolean.
        """
        return super().is_to_buy(prop) and prop.to_rent > 50
