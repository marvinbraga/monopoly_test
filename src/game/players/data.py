# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Players Data Module.
"""
from src.game.players.classes import Player, PlayerColor
from src.game.players.factories import PlayerType


class PlayerData:
    """
    Class to define players data.
    """

    @staticmethod
    def get():
        """
        Get players data.
        :return: Tuple.
        """
        return (
            Player(PlayerColor.BLUE, PlayerType.IMPULSIVE),
            Player(PlayerColor.YELLOW, PlayerType.CAUTIOUS),
            Player(PlayerColor.GREEN, PlayerType.DEMANDING),
            Player(PlayerColor.RED, PlayerType.RANDOM),
        )
