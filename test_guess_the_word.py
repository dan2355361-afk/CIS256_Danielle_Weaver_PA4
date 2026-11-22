# Danielle Weaver
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORDS,
    choose_word,
    check_guess,
    display_word
)

# Test that the randomly selected word in in our list
def test_choose_word():
    word = choose_word()
    assert word in WORDS

# Test that a correct letter is recognized
def test_correct_guess():
    assert check_guess("romance", "r") is True

# Test that an incorrect letter is recognized
def test_incorrect_guess():
    assert check_guess("fantasy", "z") is False

# Test that all repeated letters are revealed
def test_repeated_letters():
    result = display_word("paperback", {"p", "a"})
    assert result == "p a p _ _ _ a _ _"

# Test that unguessed letters stay hidden
def test_hidden_letters():
    result = display_word("dragon", {"d", "g"})
    assert result == "d _ _ g _ _"

# Test that all repeated letters are revealed correctly
def test_multiple_repeated_letters():
    result = display_word("bookkeeper", {"o", "e"})
    assert result == "_ o o _ _ e e _ e _"
