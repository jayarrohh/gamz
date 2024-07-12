import random
import time
import tkinter as tk
from word_list import *


# Makes all words in wordlist lower case
words_lower = []
for words in wordie_words:
    words_lower.append(words.lower())

class Hangman:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("CyberFirst Hangman Game")
        self.master.geometry("900x600")
        self.master.configure(bg="light blue")
        self.word_list = words_lower
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.init_gui()

    def choose_secret_word(self):
        return random.choice(self.word_list)


    def init_gui(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 30))
        self.word_display.pack(pady=(40,20))
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()

        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game, width=2, height=2,
                                    bg=button_bg, fg=button_fg, font=button_font)
        self.reset_button.pack(pady=(10,0))


    def update_canvas(self):
        self.hangman_canvas.delete("all")
        stages = [self.draw_head, self.draw_body, self.draw_leftarm, self.draw_rightarm, self.draw_leftleg, self.draw_rightleg,
                self.draw_face]
        for features in range(len(self.incorrect_guesses)):
            if features < len(stages):
                stages[features]()
        incorrect_guess_count = len(self.incorrect_gusses)

    def draw_head(self):
        self.hangman_canvas.create_over(125, 50, 185, 110, outline="black")

    def draw_body(self):
        pass

    def draw_leftarm(self):
        pass

    def draw_rightarm(self):
        pass

    def draw_leftleg(self):
        pass

    def draw_rightleg(self):
        pass

    def draw_face(self):
        pass

    def setup_alphabet_buttons(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        top_row = alphabet[:13]
        bottom_row = alphabet[13:]

        upper_frame = tk.Frame(self.buttons_frame)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons_frame)
        lower_frame.pack()

        for letter in top_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2)
            button.pack(side=("left"), padx=2, pady=2)
        
        for letter in bottom_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2)
            button.pack(side=("left"), padx=2, pady=2)

    def display_game_over_msg(self, message):
        # Hide the buttons
        self.buttons_frame.pack_forget()

        # Actually display the message
        self.game_over_label = tk.Label(self.master, text=message, font=("Helvetica", 18), fg="red")
        self.game_over_label.pack(pady=(10, 2, 0))


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

    #pick_name()

    def guess_letter(self, letter):
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas
        
        self.update_word_display()
        self.check_game_over()

    def update_word_display(self):
        displayed_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
        self.word_display.config(text=displayed_word)

    def check_game_over(self):
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations! You've won!")
        elif self.attempts_left == 0:
            self.display_game_over_message("Womp womp! Better look next time!")
            self.display_game_over_message(f"The word was {self.secret_word}")


    # Main loop

    while True:
        display_game_state()
        guess = input("Guess a letter! ").lower()

        if guess in secret_word:
            correct_guesses.add(guess)
            if set(secret_word).issubset(correct_guesses):
                print("Congratulations! You've won!")
                print(f"The word was {secret_word}")
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