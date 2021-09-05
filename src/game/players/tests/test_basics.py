# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Properties Basics Tests Module.
"""
import pytest

from src.game.utils.dices import Dice
from src.core.settings import BONUS
from src.game.properties.classes import Property
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


def test_player_bonus_receive(players):
    player = players[0]
    balance = player.balance
    player.receive_bonus(BONUS)
    assert player.balance == balance + BONUS


def test_player_pay_rent(players, properties):
    p1 = players[0]
    p2 = players[1]
    prop = properties[0]
    p1.buy(prop)
    dice_value = Dice().roll
    value = prop.to_rent(dice_value)
    balance = p2.balance
    p2.pay_rent(prop, dice_value)
    assert p2.balance == balance - value
