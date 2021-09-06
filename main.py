# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Main Module.
"""
from src.game.boards.classes import MonopolyBoard
from src.game.observers.classes import ConsoleObserver
from src.game.players.data import PlayerData
from src.game.properties.data import PropertyData
from src.game.worlds import Monopoly

if __name__ == '__main__':
    Monopoly(
        MonopolyBoard(PlayerData.get_shuffled(), PropertyData.get()),
        [ConsoleObserver()]
    ).start()
