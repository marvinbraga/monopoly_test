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

    def __init__(self, index, prop):
        self._index = index
        self._property = prop
        self._players = []

    def __str__(self):
        return f'[{self.__class__.__name__}] Idx: {self._index}, ' \
               f'Players Count: {len(self._players)}, Property: {self._property}'

    def __repr__(self):
        return str(self)

    @property
    def index(self):
        """
        Get index value.
        :return: Int.
        """
        return self._index

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

    def is_player_in(self, player):
        """
        Verify if player is in the position.
        :param player: Object.
        :return: Boolean.
        """
        return player in self._players

    def get_property(self):
        """
        Return property object.
        :return: Object.
        """
        return self._property
