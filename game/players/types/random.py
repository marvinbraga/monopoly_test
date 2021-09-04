# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Random Player Type Module.
"""
import random

from game.players.types.bases import BasePlayerType


class Random(BasePlayerType):
    """
    Class to random player type.
    """

    def is_to_buy(self, prop):
        """
        Check if the player is to buy the property.
        :param prop: Property Object.
        :return: Boolean.
        """
        return super().is_to_buy(prop) and random.choice([True, False])
