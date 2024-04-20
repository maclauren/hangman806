# task 1

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.list_of_guesses = []

# task 2

def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
        print(f"Good guess! {guess} is in the word.")

def ask_for_input(self):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)
            return guess
        
hangman_game = Hangman(["apple", "banana", "orange"])
guess = hangman_game.ask_for_input()
print("Guessed letter: ", guess)