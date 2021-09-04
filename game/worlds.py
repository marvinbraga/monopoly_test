# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game World Module.
"""
from game.utils.dices import Dice


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

    def start(self):
        """
        Run the game.
        :return: Self.
        """
        for p in self._board.players:
            print(p)

        print(self._board)
        return self
