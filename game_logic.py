import random
from ascii_art import STAGES
from game_data import WORDS


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """This function displays the game state such as the current stage of ASCII art and also
     displays the guessed letter and the letters which are not guessed yet."""
    print(f'{STAGES[mistakes]}\n')

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """
        Run the game logic:
        - Get a random word
        - Prompt the user to guess letters
        - Track mistakes and guessed letters
        - End the game when the user either guesses the word or reaches the mistake limit
        - Ask the user if they want to play again
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    MAXIMUM_MISTAKES = 3

    while mistakes < MAXIMUM_MISTAKES and not all(letter in guessed_letters for letter in secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_validated_guess_input()
        if guess not in secret_word:
            mistakes += 1
        elif guess not in guessed_letters:
            guessed_letters.append(guess)

    if mistakes == MAXIMUM_MISTAKES:
        print(f"Game Over! The word was: {secret_word} \n")
        print(STAGES[-1])
    else:
        print(f'Congratulations, you saved the snowman! \n')

    play_again()


def play_again():
    """This function prompts the user to play again."""
    user_input = input('Do you want to play again? (y/n)...\n').lower()
    if user_input == 'y':
        play_game()
    else:
        print('Thank you for playing!\n')
        exit()


def get_validated_guess_input():
    """Validate that the input is a single alphabetical character."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a single alphabetical character.")




