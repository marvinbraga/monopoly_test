# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game Boards Module.
"""
from core.settings import MAXIMUM_NUMBER_PROPERTIES
from game.boards.exceptions import MaximumNumberExceeded
from game.boards.positions import BoardPosition


class MonopolyBoard:
    """
    Class to simulate the board of Monopoly game.
    """

    def __init__(self, players, properties):
        self._players = players
        self._properties = properties
        self._check()._init_board()

    def __str__(self):
        return ''.join([str(p) + '\n' for p in self._properties])

    def _init_board(self):
        """
        Initialize board.
        :return: Self.
        """
        self._positions = [BoardPosition(prop) for prop in self._properties]
        start_position = BoardPosition(None)
        for player in self._players:
            start_position.add_player(player)
        self._positions.insert(0, start_position)
        return self

    def _check(self):
        """
        Performs board initialization checks.
        :return: Self.
        """
        if len(self._properties) > MAXIMUM_NUMBER_PROPERTIES:
            raise MaximumNumberExceeded()
        return self

    @property
    def players(self):
        """
        Return the property players.
        :return: Tuple.
        """
        return self._players
