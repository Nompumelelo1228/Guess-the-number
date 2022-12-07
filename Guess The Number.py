# own twist
import random

# the players guesses at the start of the game
player_guesses = 0

# getting random numbers from 1 to 10
number = random.randint(1, 10)

# ignore for now
""" while True:
    player_name = input('What is your player_name? ')
    print(f'Hello {player_name}, would you like to play a game? ')
    play_game = input()
    if play_game == 'yes':
        break
    else:
        print('Okay')
        exit() """

# getting player name using the input function
player_name = input("What is your player_name? ")


play_game = input(f"Hello {player_name}, would you like to play a game? (yes/no): ")

# getting player response if yes the game continues, if no then the game exits with a message
match play_game:
    case "yes" | "Yes" | "YES" | "y" | "Y":
        print(f"Well {player_name}, I am thinking of a number between 1 and 10")
    case "no" | "No" | "NO" | "n" | "N":
        print("Okay.")
        exit()
    case _:
        print("Invalid response")
        exit()

# player only has 7 guesses
for player_guesses in range(7):
    guess = int(input("Take a guess: "))

    if guess > number:
        print("Your guess is high.")

    elif guess < number:
        print("Your guess is low.")

    elif guess == number:
        break

if guess == number:
    player_guesses += 1
    if player_guesses == 1:
        print(
            f"Congratulations {player_name}. You guessed the number in {player_guesses} guess."
        )
    else:
        print(
            f"Congratulations {player_name}. You guessed the number in {player_guesses} guesses."
        )

if guess != number:
    print(
        f"Unforunately {player_name}, you weren't able to guess the number. The number that I was thinking of was {number}."
    )
