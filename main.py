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

def main_menu():
    current_player = None

    while True:
        print("1. Create new player")
        print("2. List all players")
        print("3. Select player")
        if current_player:
            print(f"4. Play Game ({current_player.username})")
            print("5. View my stats")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            if find_player_by_username(username):
                print("Username taken!")
            else:
                new_player = Player(username)
                new_player.save()
                current_player = new_player
                print(f"Player {username} created!")

        elif choice == "2":
            players = get_all_players()
            if players:
                for player in players:
                    print(f"{player.username}")
            else:
                    print("No players found")

        
        elif choice == "3":
            username = input("Enter username: ").strip()
            player = find_player_by_username(username)
            if player:
                current_player = player
                print(f"Hello {current_player.username}")
            else:
                print("Player not found")

        elif choice == "4" and current_player:
            print("Guess my 4-digit number")
            secret_number = generate_secret_number()
            guesses = 0
            won = False

            new_game = Game(current_player.id, secret_number)
            new_game.save()

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
                    new_game.status = "won"
                    new_game.guesses_taken = guesses
                    print(f"You won in {guesses} guesses!")

            if not won:
                new_game.status = "lost"
                new_game.guesses_taken = guesses
                print(f"Game over! Number was {secret_number}")

            new_game.update()
            print("Game saved!")
        
        elif choice == "5" and current_player:
            games = get_games_by_player(current_player.id)
            if games:
                wins = sum(1 for game in games if game.status == 'won')
                total = len(games)
                print(f"{current_player.username} Stats:")
                print(f"Games: {total}")
                print(f"Wins: {wins}")
            else:
                print("No games played")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name == "__main__":
    initialize_database()
    main_menu()

                
