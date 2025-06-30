import random
from ascii_art import STAGES
from game_data import WORDS


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    MAXIMUM_MISTAKES = 3

    while mistakes < MAXIMUM_MISTAKES and not all(letter in guessed_letters for letter in secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if guess not in secret_word:
            mistakes += 1
        elif guess not in guessed_letters:
            guessed_letters.append(guess)

    if mistakes == MAXIMUM_MISTAKES:
        print(f"Game Over! The word was: {secret_word}")
        print(STAGES[-1])
    else:
        print(f'Congratulations, you saved the snowman!')


