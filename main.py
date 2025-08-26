import random
from models.player import create_player_table, find_player_by_username, get_all_players, Player
from models.game import get_games_by_player, create_game_table, Game

def initialize_database():
    create_player_table()
    create_game_table()

def generate_secret_number():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])

def check_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows