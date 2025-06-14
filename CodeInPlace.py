import tkinter as tk
import random

# Global variables
buttons = []
symbols = []
first = None
second = None
matched = []

# Handle card click
def on_click(index):
    global first, second

    if index in matched or buttons[index]["text"] != " ":
        return

    buttons[index].config(text=symbols[index])

    if first is None:
        first = index
    elif second is None:
        second = index
        root.after(500, check_match)

# Check if the two revealed cards match
def check_match():
    global first, second

    if symbols[first] == symbols[second]:
        matched.extend([first, second])
    else:
        buttons[first].config(text=" ")
        buttons[second].config(text=" ")

    first = None
    second = None

    if len(matched) == 16:
        win_label.config(text="🎉 You Win!")

# Start or restart the game
def start_game():
    global buttons, symbols, matched, first, second

    matched = []
    first = None
    second = None
    win_label.config(text="")

    base = ['🍎', '🍊', '🍌', '🍉', '🍇', '🍓', '🍒', '🥝']
    symbols = base * 2
    random.shuffle(symbols)

    for i in range(16):
        buttons[i].config(text=" ", state="normal", bg="SystemButtonFace")

# Create the window
root = tk.Tk()
root.title("Simple Memory Game")

# Win message label
win_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
win_label.grid(row=0, column=0, columnspan=4, pady=10)

# Create 4x4 grid of buttons
for i in range(16):
    btn = tk.Button(root, text=" ", width=6, height=3,
                    font=("Arial", 16), command=lambda idx=i: on_click(idx))
    btn.grid(row=1 + i // 4, column=i % 4, padx=5, pady=5)
    buttons.append(btn)

# Restart button
restart_btn = tk.Button(root, text="Restart Game", command=start_game,
                        font=("Arial", 12), bg="lightblue")
restart_btn.grid(row=5, column=0, columnspan=4, pady=10)

# Start the game
start_game()
root.mainloop()


