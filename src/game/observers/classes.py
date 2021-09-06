# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Observer to Console Print Module.
"""
from src.core.observer.abstracts import AbstractObserver
from src.core.settings import ROUND_LIMIT
from src.game.players.factories import PlayerType


class ConsoleObserver(AbstractObserver):
    """
    Class to Print informations in Console.
    """

    def __init__(self):
        self._info = {
            'total_matches': 0,
            'total_turns': 0,
            'matches_per_time_out': 0,
            'average_of_turns_for_a_game': 0.0,
            'win_rate_by_player_type': None,
        }

    def update(self, value):
        """
        Update info attribute.
        :param value: AbstractSubject Object.
        :return: Self.
        """
        self._info['total_matches'] = value.total_matches
        self._info['total_turns'] = value.total_turns
        self._info['matches_per_time_out'] = value.matches_per_time_out
        self._info['average_of_turns_for_a_game'] = value.average_of_turns_for_a_game
        self._info['win_rate_by_player_type'] = value.win_rate_by_player_type
        self.display()
        return self

    def _get_percent(self, players, player_type) -> str:
        return '{0:.2f}'.format(players[player_type] / self._info['total_matches'] * 100)

    def _get_players(self) -> dict:
        return self._info['win_rate_by_player_type']

    def display(self):
        """
        Display information in console.
        :return: Self.
        """
        players = self._get_players()
        print(f'Quantas partidas terminam por time-out ({ROUND_LIMIT} rodadas):',
              '{0:.2f}'.format(self._info['matches_per_time_out']))
        print('Quantos turnos, em média, demora uma partida:',
              '{0:.2f}'.format(self._info['average_of_turns_for_a_game']))
        print('Qual a porcentagem de vitórias por comportamento dos jogadores:')
        print(f"  > {PlayerType.IMPULSIVE.value[1]} = "
              f"{players[PlayerType.IMPULSIVE]} ({self._get_percent(players, PlayerType.IMPULSIVE)}%)")
        print(f"  > {PlayerType.DEMANDING.value[1]}  = "
              f"{players[PlayerType.DEMANDING]} ({self._get_percent(players, PlayerType.DEMANDING)}%)")
        print(f"  > {PlayerType.CAUTIOUS.value[1]} = "
              f"{players[PlayerType.CAUTIOUS]} ({self._get_percent(players, PlayerType.CAUTIOUS)}%)")
        print(f"  > {PlayerType.RANDOM.value[1]} = "
              f"{players[PlayerType.RANDOM]} ({self._get_percent(players, PlayerType.RANDOM)}%)")
        print(f"Qual o comportamento que mais vence: {max(players, key=players.get)}")
        print('=====================================================================================================')
        return self
