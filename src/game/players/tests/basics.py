# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Properties Basics Tests Module.
"""
import pytest

from game.properties.classes import Property
from src.game.players.data import PlayerData
from src.game.properties.data import PropertyData


@pytest.fixture
def properties():
    """
    Prepare properties data.
    :return: Tuple.
    """
    return PropertyData.get()


@pytest.fixture
def players():
    """
    Prepare players data.
    :return: Tuple.
    """
    return PlayerData.get()


def test_check_player_can_buy(players, properties):
    player = players[0]
    prop = properties[0]
    assert player.should_buy(prop)


def test_check_player_is_alive(players):
    player = players[0]
    assert player.is_alive


def test_check_player_cant_buy(players):
    player = players[0]
    player.buy(Property('Max Property', 300.0, 10.0))
    assert not player.should_buy(Property('Little Property', 1.0, 0.1))
