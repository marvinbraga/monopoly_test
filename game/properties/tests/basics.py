# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Properties Basics Tests Module.
"""
import pytest

from game.players.data import PlayerData
from game.properties.data import PropertyData


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
