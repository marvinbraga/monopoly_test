# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Monopoly World Tests Module.
"""
import pytest

from src.game.boards.classes import MonopolyBoard
from src.game.players.data import PlayerData
from src.game.properties.data import PropertyData
from src.game.worlds import Monopoly


@pytest.fixture
def world():
    """
    Prepare Board data.
    :return: Object.
    """
    return Monopoly(
        MonopolyBoard(PlayerData.get(), PropertyData.get())
    )


def test_check_not_a_winner(world):
    assert not world.get_winner()


def test_check_a_winner(world):
    p1 = world.board.get_next_player()
    p1._balance = -1
    p2 = world.board.get_next_player()
    p2._balance = -1
    p3 = world.board.get_next_player()
    p3._balance = -1
    assert world.get_winner()
