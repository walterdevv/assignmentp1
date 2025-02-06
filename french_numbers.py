import tkinter as tk
from tkinter import CENTER

def showFrenchNumber(number):
    frenchNumbers = {1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq"}
    lblFrench.config(text=frenchNumbers[number], fg="white", bg="green")
    lblFrench.pack()

def close_app():
    root.destroy()

root = tk.Tk()
root.title("French Numbers")
root.geometry("350x200")  
root.resizable(False, False)  
root.overrideredirect(True)  

root.eval('tk::PlaceWindow . center')

lblInstructions = tk.Label(root, text="Do you know the French words for the numbers 1 through 5?\nClick the buttons below to see them.", wraplength=320)
lblInstructions.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack()

for i in range(1, 6):
    btn = tk.Button(button_frame, text=str(i), width=4, command=lambda i=i: showFrenchNumber(i))
    btn.grid(row=0, column=i-1, padx=2)

lblFrench = tk.Label(root, text="", font=("Arial", 12, "bold"))
lblFrench.pack(pady=5)

btnExit = tk.Button(root, text="Exit", command=close_app)
btnExit.pack(pady=10)

root.mainloop()
