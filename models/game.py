from models.base import CURSOR, CONN
from datetime import datetime

class Game:

    def __init__(self, player_id, secret_number, status="in_progress", guesses_token=0, id=None):
        self.id = id
        self.player_id = player_id
        self.secret_number = secret_number
        self.status = status
        self.guesses_taken = guesses_token
        self.created_at = datetime.now()