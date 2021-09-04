# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game Board Position Module.
"""


class BoardPosition:
    """
    Class to define Board Position.
    """

    def __init__(self, prop):
        self._property = prop
        self._players = []

    def add_player(self, player):
        """
        Method to add player in board position.
        :param player: Player object.
        :return: Self.
        """
        self._players.append(player)
        return self

    def remove_player(self, player):
        """
        Method to remove player on board position.
        :param player: Player object.
        :return: Self.
        """
        self._players.remove(player)
        return self
