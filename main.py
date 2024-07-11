import random
import time
import tkinter as tk
from word_list import *


# Makes all words in wordlist lower case
words_lower = []
for words in wordie_words:
    words_lower.append(words.lower())

# Random choice from lower case word listpyt
secret_word = random.choice(words_lower)
correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6


class Hangman:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("CyberFirst Hangman Game")
        self.master.geometry("900x600")

        # Add More UI stuff here later

def pick_name():
    name = input("Hello there! What is your name? ")
    time.sleep(.5)
    name_lower = name.lower()
    
    if name_lower in banned_cut:
        print("This name is banned, choose another")
        pick_name()
    else:
        print(f"Nice to meet you, {name}! Let's play Cyber Hangman!")

pick_name()


def display_game_state():
    displayed_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"Word: {displayed_word}")
    print(f"Incorrect Guesses: {' '.join(incorrect_guesses)}")
    print(f"Attempts Left: {attempts_left}")

# Main loop

while True:
    display_game_state()
    guess = input("Guess a letter! ").lower()

    if guess in secret_word:
        correct_guesses.add(guess)
        if set(secret_word).issubset(correct_guesses):
            print("Congratulations! You've won!")
            break
    else:
        if guess not in incorrect_guesses:
            incorrect_guesses.add(guess)
            attempts_left -= 1
        else:
            print("You already guessed that!")
        if attempts_left == 0:
            print("Womp womp! Better luck next time!")
            print(f"The answer was {secret_word}!")
            break


def main():
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()

if __name__ == "__main__":
    main()