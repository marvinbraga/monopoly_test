# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game Boards Module.
"""
import copy
import itertools

from src.core.settings import MAXIMUM_NUMBER_PROPERTIES
from src.game.boards.exceptions import MaximumNumberExceeded
from src.game.boards.positions import BoardPosition


class MonopolyBoard:
    """
    Class to simulate the board of Monopoly game.
    """

    def __init__(self, players, properties):
        self._players_clean = copy.deepcopy(players)
        self._properties_clean = copy.deepcopy(properties)
        self._players = copy.deepcopy(players)
        self._properties = copy.deepcopy(properties)
        self._positions = []
        self._iter_players = None
        self._check()._init_board()

    def __str__(self):
        return ''.join([str(p) + '\n' for p in self._properties])

    def _init_board(self):
        """
        Initialize board.
        :return: Self.
        """
        self._players = copy.deepcopy(self._players_clean)
        self._iter_players = itertools.cycle(self._players)
        self._properties = copy.deepcopy(self._properties_clean)
        self._positions = []
        start_position = BoardPosition(0, None)
        for player in self._players:
            start_position.add_player(player)
        self._positions.append(start_position)
        index = 0
        for prop in self._properties:
            index += 1
            self._positions.append(BoardPosition(index, prop))
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
        :return: List.
        """
        return self._players

    @property
    def properties(self):
        """
        Return the property properties.
        :return: Tuple.
        """
        return self._properties

    def reset_board(self):
        """
        Reset board information.
        :return: Self.
        """
        self._init_board()
        return self

    def get_player_position(self, player):
        """
        Returns the player position int the board.
        :param player: Object.
        :return: Position Object.
        """
        return next(pos for pos in self._positions if pos.is_player_in(player))

    def get_next_player(self):
        """
        Get Next Alive Player from Iter.
        :return: Player Object.
        """
        while True:
            player = next(self._iter_players)
            if player.is_alive:
                break
        return player

    def move_player(self, player, number):
        """
        Move player in board.
        :param player: Player object.
        :param number: Number of squares on the board to walk.
        :return: Position Object.
        """
        position = self.get_player_position(player)
        position.remove_player(player)
        index = position.index + number
        if index > len(self._positions) - 1:
            index -= len(self._positions)
        position = self._positions[index]
        position.add_player(player)
        return position
