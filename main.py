import random
from models.player import create_player_table, find_player_by_username, get_all_players, Player
from models.game import get_games_by_player, create_game_table, Game

def initialize_database():
    create_player_table()
    create_game_table()

