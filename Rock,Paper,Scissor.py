import tkinter as tk
import random

# Function to determine the winner
def game(me, c):
    if me == c:
        return "It's a tie!"
    elif c == 'Rock':
        if me == 'Scissors':
            return "You lose"
        elif me == 'Paper':
            return "You win"
    elif c == 'Paper':
        if me == 'Rock':
            return "You lose"
        elif me == 'Scissors':
            return "You win"
    elif c == 'Scissors':
        if me == 'Paper':
            return "You lose"
        elif me == 'Rock':
            return "You win"

# Function to handle user's choice
def make_choice(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    c = random.choice(computer_choices)
    result = game(choice, c)
    result_label.config(text=f"Computer chose: {c}\n{result}")

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("Rock, Paper, Scissors")
root.configure(bg="black")

# Create labels and buttons
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:",font= ("Arial",20),bg = "light green")
instruction_label.pack(pady=5)

rock_button = tk.Button(root, text="Rock", command=lambda: make_choice("Rock"),font= ("Arial",20),bg = "light green")
paper_button = tk.Button(root, text="Paper", command=lambda: make_choice("Paper"),font= ("Arial",20),bg = "light green")
scissors_button = tk.Button(root, text="Scissors", command=lambda: make_choice("Scissors"),font= ("Arial",20),bg = "light green")

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="",font= ("Arial",20),bg = "light pink")
result_label.pack(pady=5)

# Start the GUI main loop
root.mainloop()
