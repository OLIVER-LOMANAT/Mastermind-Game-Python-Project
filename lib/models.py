from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///bulls_and_bulls.db')
Session = sessionmaker(bind=engine)
session = Session()

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # One-to-many relationship: one player has many games
    games = relationship("Game", back_populates="player")
    
    def __repr__(self):
        return f"<Player {self.username}>"

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    secret_number = Column(String, nullable=False)
    status = Column(String, default="in_progress")  # 'in_progress', 'won', 'lost'
    guesses_taken = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    
    # Many-to-one relationship: many games belong to one player
    player = relationship("Player", back_populates="games")
    
    def __repr__(self):
        return f"<Game {self.id}: {self.status}>"

# Create tables
Base.metadata.create_all(engine)