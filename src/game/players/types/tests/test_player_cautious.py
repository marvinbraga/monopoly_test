# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Player Cautious Tests Module.
"""
import pytest

from src.core.settings import OPENING_BALANCE
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


def test_can_buy_if_there_is_balance(players, properties):
    player = players[1]
    prop = properties[13]
    assert player.should_buy(prop)


def test_dont_buy_without_balance(players, properties):
    player = players[1]
    player.pay(OPENING_BALANCE)
    prop = properties[13]
    assert not player.should_buy(prop)


def test_dont_buy_when_balance_below_80(players, properties):
    player = players[1]
    player.pay(OPENING_BALANCE - 81)
    prop = properties[0]
    assert not player.should_buy(prop)
