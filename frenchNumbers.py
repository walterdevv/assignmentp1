"""

Walter Cooper
CPSC 3118
Assignment P1: First GUI Development Project
6 February 2025

"""

import tkinter as tk
from tkinter import CENTER

# function that displays the french translation of given number
def showFrenchNumber(number):
    frenchNumbers = {1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq"} # dictionary mapping numbers to their French equivalents
    lblFrench.config(text=frenchNumbers[number], fg="white", bg="green") # updates label with the French word and sets the text color to white with a green background
    lblFrench.pack()

def closeApp(): # function which closes the application
    root.destroy()

root = tk.Tk() # initializes the main application window
root.title("French Numbers") # sets the window title
root.geometry("350x200")   # sets a fixed window size
root.resizable(False, False)   # disables window resizing
root.overrideredirect(True)   # removes default window decorations such as the border and close button (bonus points section)

root.eval('tk::PlaceWindow . center') # centers the winodw on the screen

# this is the instruction label which can be seen upon immediately opening the program
lblInstructions = tk.Label(root, text="Do you know the French words for the numbers 1 through 5?\nClick the buttons below to see them.", wraplength=320)
lblInstructions.pack(pady=5)

buttonFrame = tk.Frame(root) # frame to hold number buttons
buttonFrame.pack()

for i in range(1, 6): # iteration to create buttons for numbers 1-5 and then it adds them to the frame
    btn = tk.Button(buttonFrame, text=str(i), width=4, command=lambda i=i: showFrenchNumber(i))
    btn.grid(row=0, column=i-1, padx=2)

lblFrench = tk.Label(root, text="", font=("Arial", 12, "bold")) # label that displays the french translations
lblFrench.pack(pady=5)

btnExit = tk.Button(root, text="Exit", command=closeApp) # exit button
btnExit.pack(pady=10)

root.mainloop() # main loop
