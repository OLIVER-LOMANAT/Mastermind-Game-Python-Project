#!/usr/bin/env python3

from helpers import *
from models import session

def main_menu():
    current_player = None
    
    while True:
        print("\n--- Bulls & Cows Game ---")
        print("1. Create new player")
        print("2. List all players")
        print("3. Select player")
        if current_player:
            print(f"4. Play game ({current_player.username})")
            print("5. View my stats")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            if find_player_by_username(username):
                print("Username taken!")
            else:
                current_player = create_player(username)
                print(f"Player {username} created!")

        elif choice == "2":
            players = get_all_players()
            if players:
                for player in players:
                    print(f"- {player.username}")
            else:
                print("No players found")

        elif choice == "3":
            username = input("Enter username: ").strip()
            player = find_player_by_username(username)
            if player:
                current_player = player
                print(f"Hello {current_player.username}!")
            else:
                print("Player not found")

        elif choice == "4" and current_player:
            print("\nNew game started!")
            secret_number = generate_secret_number()
            guesses = 0
            won = False

            # Create game with SQLAlchemy
            game = Game(
                player_id=current_player.id,
                secret_number=secret_number,
                status="in_progress"
            )
            session.add(game)
            
            while guesses < 10 and not won:
                guess = input(f"Guess #{guesses + 1}: ").strip()
                
                if len(guess) != 4 or not guess.isdigit():
                    print("Enter 4-digit number")
                    continue
                
                guesses += 1
                bulls, cows = check_guess(secret_number, guess)
                print(f"{bulls} Bulls, {cows} Cows")

                if bulls == 4:
                    won = True
                    game.status = "won"
                    game.guesses_taken = guesses
                    print(f"You won in {guesses} guesses!")

            if not won:
                game.status = "lost"
                game.guesses_taken = guesses
                print(f"Game over! Number was {secret_number}")

            session.commit()
            print("Game saved!")

        elif choice == "5" and current_player:
            games = get_player_games(current_player.id)
            if games:
                wins = sum(1 for game in games if game.status == 'won')
                total = len(games)
                print(f"\n{current_player.username}'s Stats:")
                print(f"Games: {total}")
                print(f"Wins: {wins}")
                print(f"Win %: {wins/total*100:.1f}%" if total > 0 else "Win %: 0%")
            else:
                print("No games played")

        elif choice == "6":
            print("Goodbye!")
            session.close()
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()