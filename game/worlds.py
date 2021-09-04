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

    def __init__(self, players, board):
        self._board = board
        self._players = players
        self._dices = (Dice(),)

    def roll_dices(self):
        """
        Method to roll the dices.
        :return: Tuple with values.
        """
        return (dice.roll for dice in self._dices)
