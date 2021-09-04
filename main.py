# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Main Module.
"""
from game.boards.classes import MonopolyBoard
from game.players.data import PlayerData
from game.properties.data import PropertyData
from game.worlds import Monopoly

if __name__ == '__main__':
    Monopoly(
        MonopolyBoard(PlayerData.get(), PropertyData.get())
    ).start()
