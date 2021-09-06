# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Properties Basics Tests Module.
"""
import pytest

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


def test_properties_data_charge(properties):
    assert properties
    assert isinstance(properties, list)


def test_players_data_charge(players):
    assert players
    assert isinstance(players, list)


def test_add_owner_to_property(players, properties):
    player = players[0]
    prop = properties[0]
    if player.should_buy(prop):
        player.buy(prop)
    assert prop.owner is player


def test_is_property_free(properties):
    prop = properties[0]
    assert prop.owner is None
