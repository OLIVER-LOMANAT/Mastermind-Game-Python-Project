from models.base import CURSOR, CONN

class Player:

    def __init__(self, username, id=None):
        self.id = id
        self.username = username

    def __repr__(self):
        return f"Player {self.id}: {self.username}"
    
    def save(self):
        sql = "INSERT INTO players (username) VALUES (?)"
        CURSOR.execute(sql, (self.username))
        CONN.commit()
        self.id = CURSOR.lastrowid

