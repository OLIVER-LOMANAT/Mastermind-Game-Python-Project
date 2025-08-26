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

def create_player_table():
    sql = """
        CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE
        )
    """
    CURSOR.execute(sql)
    CONN.commit()

def get_all_players():
    sql = "SELECT * FROM players"
    CURSOR.execute(sql)
    rows = CURSOR.fetchall()
    players = []
    for row in rows:
        player = Player(row[1], row[0])
        players.append(player)
    return players


def find_player_by_username(username):
    sql = "SELECT * FROM players WHERE username = ?"
    CURSOR.execute(sql, (username,))
    row = CURSOR.fetchone()
    if row:
        return Player(row[1], row[0])
    return None

