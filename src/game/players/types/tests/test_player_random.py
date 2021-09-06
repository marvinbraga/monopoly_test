# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Player Random Tests Module.
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
    player = players[3]
    prop = properties[13]
    buy = player.should_buy(prop)
    if buy:
        assert buy
    else:
        assert not buy


def test_dont_buy_without_balance(players, properties):
    player = players[3]
    player.pay(OPENING_BALANCE)
    prop = properties[13]
    assert not player.should_buy(prop)
