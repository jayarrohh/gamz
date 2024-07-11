import random
import time
import tkinter as tk
from word_list import wordie_words

# Choose random word from imported dictionary
secret_word = random.choice(wordie_words)
correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6

class Hangman:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("CyberFirst Hangman Game")
        self.master.geomtry("900x600")
        # Add More UI stuff here later

#name = input("Hello there! What is your name? ")

#time.sleep(1)

#print(f"Nice to meet you, {name}! Let's player Cyber Hangman!")


def display_game_state():
    displayed_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"Word: {displayed_word}")
    print(f"Incorrect Guesses: {" ".join(incorrect_guesses)}")
    print(f"Attempts Left: {attempts_left}")

# Main loop
while True:
    display_game_state()
    guess = input("Guess a letter! ").lower

    if str(guess) in secret_word:
        correct_guesses.add(guess)
        if set(secret_word).issubset(correct_guesses):
            print("Congratulations! You've won!")
            break
    else:
        incorrect_guesses.add(guess)
        attempts_left -= 1
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