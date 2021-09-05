# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Game World Module.
"""
from src.core.settings import ROUND_LIMIT, BONUS
from src.game.exceptions import GameIsOver
from src.game.utils.dices import Dice


class Monopoly:
    """
    Class to Monopoly World.
    """

    def __init__(self, board):
        self._board = board
        self._dices = (Dice(),)
        self._winner = None

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
        result = None
        value = 0
        for player in self._board.players:
            if player.balance >= value:
                result = player
                value = player.balance
        return result

    def start(self):
        """
        Run the game.
        :return: Self.
        """
        for game_round in range(ROUND_LIMIT):
            player = self._board.get_next_player()
            if self.check_winner(player):
                raise GameIsOver(f'The player {player} outperformed all others and was THE WINNER!')

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

        player = self.get_best_player()
        raise GameIsOver(f'The player {player} was THE WINNER!')
