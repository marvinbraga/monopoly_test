# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Boards Exceptions Module.
"""
from core.exceptions import GameBaseException


class MaximumNumberExceeded(GameBaseException):
    """
    Exception to To indicate the maximum number of properties has been exceeded.
    """
    def __init__(self):
        super().__init__('The maximum number of properties has been exceeded.')
