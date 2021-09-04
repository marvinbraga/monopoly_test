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
    """
    Test data initialization.
    :param properties: properties fixture.
    :return: None.
    """
    assert properties
    assert isinstance(properties, tuple)


def test_players_data_charge(players):
    """
    Test data initialization.
    :param players: players fixture.
    :return: None.
    """
    assert players
    assert isinstance(players, tuple)


def test_add_owner_to_property(players, properties):
    """
    Test to check the process to add a player owner to a property.
    :param players: Tuple.
    :param properties: Tuple.
    :return: None.
    """
    player = players[0]
    prop = properties[0]
    if player.should_buy(prop):
        player.buy(prop)
    assert prop.owner is player


def test_is_property_free(properties):
    """
    Verify if property don't have an owner.
    :param properties: Tuple.
    :return: None.
    """
    prop = properties[0]
    assert prop.owner is None
