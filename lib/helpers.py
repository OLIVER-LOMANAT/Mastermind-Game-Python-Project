import random
from models import session, Player, Game

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

def create_player(username):
    player = Player(username=username)
    session.add(player)
    session.commit()
    return player

def get_all_players():
    return session.query(Player).all()

def find_player_by_username(username):
    return session.query(Player).filter(Player.username == username).first()

def get_player_games(player_id):
    return session.query(Game).filter(Game.player_id == player_id).all()