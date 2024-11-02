import tkinter as tk
import random

# Function to roll the dice and update the display
def roll_dice():
    # Generate random dice values between 1 and 6
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
   
    # Update the dice labels to display the results
    dice1_label.config(text=str(dice1))
    dice2_label.config(text=str(dice2))
   
    # Update the result label with the total of both dice
    result_label.config(text=f"Total: {dice1 + dice2}")

# Initialize the main application window
root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x200")  # Set window size

# Set a theme color for the background
root.configure(bg="#2E4053")  # Dark blue background

# Header label to instruct the user
header_label = tk.Label(
    root, text="Welcome to the Dice Roller!", font=("Arial", 14),
    fg="#FAD02E", bg="#2E4053"
)
header_label.pack(pady=10)

# Labels to display each dice value
dice1_label = tk.Label(
    root, text="0", font=("Arial", 24), fg="white", bg="#2E4053"
)
dice1_label.pack(side="left", padx=20, pady=20)

dice2_label = tk.Label(
    root, text="0", font=("Arial", 24), fg="white", bg="#2E4053"
)
dice2_label.pack(side="right", padx=20, pady=20)

# Button to roll the dice
roll_button = tk.Button(
    root, text="Roll Dice", font=("Arial", 14), command=roll_dice,
    fg="#2E4053", bg="#FAD02E", activebackground="#FAD02E",
    activeforeground="#2E4053"
)
roll_button.pack(pady=10)

# Label to display the total result of both dice
result_label = tk.Label(
    root, text="Total: 0", font=("Arial", 14), fg="#FAD02E", bg="#2E4053"
)
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

