# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Subject to Observers Module.
"""
from src.core.observer.abstracts import AbstractSubject
from src.game.players.factories import PlayerType


class GameInformations(AbstractSubject):
    """
    Class to describe the game information.
    """
    def __init__(self):
        self._total_matches = 0
        self._total_turns = 0
        self._matches_per_time_out = 0
        self._average_of_turns_for_a_game = 0.0
        self._win_rate_by_player_type = {
            PlayerType.IMPULSIVE: 0,
            PlayerType.DEMANDING: 0,
            PlayerType.CAUTIOUS: 0,
            PlayerType.RANDOM: 0,
        }

    @property
    def total_matches(self):
        """
        Number of total matches.
        :return: Int.
        """
        return self._total_matches

    @property
    def total_turns(self):
        """
        Number of total turns.
        :return: Int.
        """
        return self._total_turns

    @property
    def matches_per_time_out(self):
        """
        How many matches finish per time out (1000 rounds);
        :return: Int.
        """
        return self._matches_per_time_out

    @property
    def average_of_turns_for_a_game(self):
        """
        How many turns on average takes a game.
        :return: Float.
        """
        return self._average_of_turns_for_a_game

    @property
    def win_rate_by_player_type(self):
        """
        Number of wins by player behavior;
        :return: Dict.
        """
        return self._win_rate_by_player_type

    def set_info(self, total_matches: int, total_turns: int, matches_per_time_out: int,
                 average_of_turns_for_a_game: float, win_rate_by_player_type: dict):
        """
        Update all information.
        :param total_matches: Int.
        :param total_turns: Int.
        :param matches_per_time_out: Int.
        :param average_of_turns_for_a_game: Float.
        :param win_rate_by_player_type: Dict.
        :return: Self.
        """
        self._total_matches = total_matches
        self._total_turns = total_turns
        self._matches_per_time_out = matches_per_time_out
        self._average_of_turns_for_a_game = average_of_turns_for_a_game
        self._win_rate_by_player_type = win_rate_by_player_type
        self.notify(self)
