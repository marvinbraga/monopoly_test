# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Board Basic Tests Module.
"""
import pytest

from src.game.boards.classes import MonopolyBoard
from src.game.players.data import PlayerData
from src.game.properties.data import PropertyData


@pytest.fixture
def board():
    """
    Prepare Board data.
    :return: Object.
    """
    return MonopolyBoard(PlayerData.get(), PropertyData.get())


def test_init_board(board):
    assert board


def test_player_in_start_position(board):
    player = board.players[0]
    position = board.get_player_position(player)
    assert position.get_property() is None


def test_player_move_in_board(board):
    player = board.players[0]
    board.move_player(player, 2)
    position = board.get_player_position(player)
    assert position.get_property()


def test_player_passes_the_start_point(board):
    player = board.players[0]
    pos1 = board.move_player(player, 10)
    pos2 = board.move_player(player, 11)
    assert pos2.index < pos1.index
    assert pos1.index == 10
    assert pos2.index == 0
