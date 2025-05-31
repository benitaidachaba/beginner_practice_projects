# This is a simple number guessing game implemented using Python's Tkinter library for GUI.
import random
import tkinter as tk

#setting up the main window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("300x300")

# Function to handle the window close event
def on_close():
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_close)

#generate a random number between 1 and 10 and ask the user to guess it
secret_number = random.randint(1, 10)
# guess = int(input("Enter the secret number:"))
guess_count = 0

# function to check the user's guess, compare it with the secret number, and provide feedback, if its wrong this program will prompt the user to try again until they guess the correct number and also add 1 to the guess count each time the user makes a guess.
def check_guess():
    global guess_count
    guess = int(guess_entry.get())
    guess_count += 1

#for the if statement, if the guess is correct, show success message and disable the guess button then prompt the user to play again.
    if guess == secret_number:
        result_label.config(text=f"Congratulations! You guessed it in {guess_count} tries!")
        # Disable the guess button and show the play again button if the guess is correct
        guess_button.config(state=tk.DISABLED)
        play_again_button.pack()
    elif guess > 10 or guess < 1:
        result_label.config(text="Oops, your guess is out of bounds! Please guess a number between 1 and 10.")
    elif guess > secret_number:
        result_label.config(text="Oops, your guess is too high. Try again!")
    elif guess < secret_number:
        result_label.config(text="Oops, your guess is too low. Try again!")
    else:
        result_label.config(text="Oops, your guess is incorrect. Try again!")

# Function to reset the game
def reset_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 10)
    guess_count = 0
    result_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)
    play_again_button.pack_forget()


# GUI Elements
title_label = tk.Label(root, text="Guess a number between 1 and 10", font=("times new roman", 14))
title_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 12))
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Submit Guess", command=check_guess, font=("times new roman", 12), bg="lightblue", fg="black")
guess_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("times new roman", 12), fg="red")
result_label.pack(pady=10)

play_again_button = tk.Button(root, text="🔁 Play Again", command=reset_game, font=("times new roman", 12), bg="lightgreen", fg="black")
play_again_button.pack(pady=5)

# Start the GUI loop
root.mainloop()