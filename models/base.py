import sqlite3

CONN = sqlite3.connect('bulls_and_bulls.db')
CURSOR = CONN.cursor()