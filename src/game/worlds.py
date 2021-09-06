# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game World Module.
"""
import copy

from src.core.settings import ROUND_LIMIT, BONUS
from src.game.exceptions import GameIsOver
from src.game.observers.subjects import GameInformations
from src.game.players.factories import PlayerType
from src.game.utils.dices import Dice


class Monopoly:
    """
    Class to Monopoly World.
    """

    def __init__(self, board, observers=None):
        self._board = board
        self._dices = (Dice(),)
        self._winner = None
        self._game_informations = GameInformations()
        self._infos = self._init_informations()
        if observers:
            self._attach_observers(observers)

    def _attach_observers(self, observers):
        for observer in observers:
            self._game_informations.attach(observer)

    def _init_informations(self):
        return {
            'total_turns': self._game_informations.total_turns,
            'matches_per_time_out': self._game_informations.matches_per_time_out,
            'win_player_type': None,
        }

    @property
    def board(self):
        """
        Get board attribute.
        :return: Board Object.
        """
        return self._board

    def roll_dices(self):
        """
        Method to roll the dices.
        :return: Int.
        """
        return sum([dice.roll for dice in self._dices])

    @property
    def winner(self):
        """
        Get the game winner player.
        :return: Player Object.
        """
        return self._winner

    def get_active_players(self):
        """
        Return only active players with positive balance.
        :return: List.
        """
        return [player for player in self._board.players if player.is_alive]

    def get_winner(self):
        """
        Return winner player.
        :return: Object.
        """
        result = None
        players = self.get_active_players()
        if len(players) == 1:
            result = players[0]
        return result

    def check_winner(self, player):
        """
        Verify Winner.
        :param player: Object.
        :return: Boolean.
        """
        return player is self.get_winner()

    def dispossess_player(self, player):
        """
        Disassociate the player from all of his properties.
        :param player: Player object.
        :return: Self.
        """
        for prop in self.board.properties:
            if prop.owner is player:
                prop.owner = None
        return self

    def check_bonus(self, player, old_position, new_position):
        """
        Pay bonus to player if passed to start point.
        :param player: Player Object.
        :param old_position: Position Object.
        :param new_position: Position Object.
        :return: Self.
        """
        if new_position.index < old_position.index:
            player.receive_bonus(BONUS)
        return self

    def get_best_player(self):
        """
        Return the best player.
        :return: Player object.
        """
        values = [player.balance for player in self._board.players]
        return self._board.players[values.index(max(values))]

    def start(self, total_simulations=300):
        """
        Run the game.
        :return: Self.
        """
        for simulation in range(total_simulations):
            try:
                self._play_game()
            except GameIsOver:
                self._update_game_informations()
        return self

    def _update_game_informations(self):
        total_matches = self._game_informations.total_matches + 1
        matches_per_time_out = self._infos['matches_per_time_out']
        average_of_turns_for_a_game = self._infos['total_turns'] / total_matches
        win_rate_by_player_type = copy.deepcopy(self._game_informations.win_rate_by_player_type)
        win_rate_by_player_type[self._infos['win_player_type']] += 1
        self._game_informations.set_info(
            total_matches, self._infos['total_turns'], matches_per_time_out,
            average_of_turns_for_a_game, win_rate_by_player_type
        )

    def _play_game(self):
        self._board.reset_board()
        self._infos = self._init_informations()
        for game_round in range(ROUND_LIMIT):
            player = self._board.get_next_player()
            if self.check_winner(player):
                self._set_win_player_type(player)
                raise GameIsOver(f'The player {player} outperformed all others and was THE WINNER!')

            self._infos['total_turns'] += 1
            dice_value = self.roll_dices()
            old_position = self._board.get_player_position(player)
            position = self._board.move_player(player, dice_value)
            self.check_bonus(player, old_position, position)

            prop = position.get_property()
            if prop and prop.owner:
                player.pay_rent(prop, dice_value)
            else:
                if player.should_buy(prop):
                    player.buy(prop)
            if player.balance < 0:
                self.dispossess_player(player)

        player = self.get_best_player()
        self._infos['matches_per_time_out'] += 1
        self._set_win_player_type(player)
        raise GameIsOver(f'The player {player} was THE WINNER!')

    def _set_win_player_type(self, player):
        self._infos['win_player_type'] = PlayerType[str(player.player_type).upper()]
