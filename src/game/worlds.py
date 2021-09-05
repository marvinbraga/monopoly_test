# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game World Module.
"""
from core.settings import ROUND_LIMIT
from src.game.utils.dices import Dice


class Monopoly:
    """
    Class to Monopoly World.
    """

    def __init__(self, board):
        self._board = board
        self._dices = (Dice(),)
        self._winner = None

    def roll_dices(self):
        """
        Method to roll the dices.
        :return: Tuple with values.
        """
        return (dice.roll for dice in self._dices)

    @property
    def winner(self):
        """
        Get the game winner player.
        :return: Player Object.
        """
        return self._winner

    def get_active_players(self):
        """
        Return only active players with positive balance.
        :return: List.
        """
        return [player for player in self._board.players if player.is_alive]

    def get_winner(self):
        """
        Return winner player.
        :return: Object.
        """
        result = None
        players = self.get_active_players()
        if len(players) == 1:
            result = players[0]
        return result

    def start(self):
        """
        Run the game.
        :return: Self.
        """
        for game_round in range(ROUND_LIMIT):
            pass

        return self
