# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Boards Exceptions Module.
"""
from core.exceptions import GameBaseException


class GameIsOver(GameBaseException):
    """
    Exception to end the game.
    """
    pass
