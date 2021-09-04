# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Player Type Factory Module.
"""
from enum import Enum

from game.players.types.cautious import Cautious
from game.players.types.demanding import Demanding
from game.players.types.impulsive import Impulsive
from game.players.types.random import Random


class PlayerType(Enum):
    """
    Class to indicate the player type.
    """
    IMPULSIVE = 0
    DEMANDING = 1
    CAUTIOUS = 2
    RANDOM = 3

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
