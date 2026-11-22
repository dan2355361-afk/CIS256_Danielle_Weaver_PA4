# Danielle Weaver
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of possible bookish words for the game
WORDS = [
    "romance",
    "fantasy",
    "mystery",
    "villian",
    "chapter",
    "bookstore",
    "dragon",
    "library",
    "fiction",
    "enemies",
    "kingdom",
    "plotwist",
    "paperback",
    "thriller",
    "epilogue"
]

MAX_ATTEMPTS = 6

# Choose a random word from the bookish word list
def choose_word():
    return random.choice(WORDS)

# Check whether a guessed letter is in the secret word
def check_guess(word, letter):
    return letter in word

# Reveal every occurence of correctly guessed letters
def display_word(word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else"_"
        for letter in word
    )

# Run the bookish word guessing game
def play_game():
    secret_word = choose_word()
    guessed_letters = set()
    attempts = MAX_ATTEMPTS

    print("\nWelcome to Between the Lines!")
    print("A Bookish Word Guessing Game")
    print("Guess the secret bookish word one letter at a time.")
    print(f"You have {attempts} incorrect guesses available.")

    while attempts > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input("Guess a letter: ").lower().strip()

        # Make sure the player enters one alphabetical letter
        if not guess:
            print("You need to enter a letter!")
            continue

        # Only accept one letter from A to Z
        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Please enter one letter from A to Z!")
            continue

        # Do not count letters that have already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if check_guess(secret_word, guess):
            print("A plot twist! That letter is in the word!")
        else:
            attempts -= 1
            print("The plot thickens... Wrong letter!")

        # Check whether every letter has been revealed
        if all(letter in guessed_letters for letter in secret_word):
            print("\nWord:", display_word(secret_word, guessed_letters))
            print("The final chapter is yours!")
            print("Congratulations! You guessed the word!")
            return

    print("\nCliffhanger! You've run out of guesses.")
    print(f"The secre word was: {secret_word}")

# Only start the game when this file is run directly
if __name__ == "__main__":
    play_game()
