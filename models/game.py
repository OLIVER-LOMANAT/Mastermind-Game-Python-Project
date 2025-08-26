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

    def __repr__(self):
        return f"Game {self.id}: Player {self.player_id}, {self.status}"
    
    def save(self):
        sql = """
            INSERT INTO games (player_id, secret_number, status, guesses_taken, created_at)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.player_id, self.secret_number, self.status, self.guesses_taken, self.created_at))
        self.id = CURSOR.lastrowid
    
    def update(self):
        sql = """
            UPDATE games SET status = ?, guesses_taken = ? WHERE id = ?
        """
        CURSOR.execute(sql, (self.status, self.guesses_taken, self.id))
        CONN.commit()
        