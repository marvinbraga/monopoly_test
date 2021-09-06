# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Player Type Factory Module.
"""
from enum import Enum

from src.game.players.types.cautious import Cautious
from src.game.players.types.demanding import Demanding
from src.game.players.types.impulsive import Impulsive
from src.game.players.types.random import Random


class PlayerType(Enum):
    """
    Class to indicate the player type.
    """
    IMPULSIVE = 0, 'Impulsivo'
    DEMANDING = 1, 'Exigente'
    CAUTIOUS = 2, 'Cauteloso'
    RANDOM = 3, 'Aleatório'

    def __str__(self):
        return self.value[1]

    def new(self, player):
        """
        Creates an instance of the type from its value.
        :argument: Player object.
        :return: Object.
        """
        result = {
            PlayerType.IMPULSIVE: Impulsive,
            PlayerType.DEMANDING: Demanding,
            PlayerType.CAUTIOUS: Cautious,
            PlayerType.RANDOM: Random,
        }[self]
        return result(player)
