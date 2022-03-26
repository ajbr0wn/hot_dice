import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

class DiceRoller(Frame):
    
    MIN_VAL = 1
    labels = []

    def __init__(self):
        tk.Frame.__init__(self)
        
        self.pack()
        self.master.geometry("400x270")

        title = "Hot Dice"
        self.master.title(title)

        dice_values = [4, 6, 8, 10, 12, 20, 100]

        for i in range(len(dice_values)):
            button = Button(self, text = 'Roll D%s'%(dice_values[i]), width = 10)
            button.grid(row = i, column = 0, padx=(5, 5), pady=(5, 5))
            
            label = Label(self, text = 0, width = 10)
            label.grid(row = i, column = 1, padx=(5, 5), pady=(5, 5))
            self.labels.append(label)

            button.configure(command = lambda i=i: self.roll(i, dice_values[i]))

    
    def roll(self, label_index, max_val):
        dice_roll = random.randint(self.MIN_VAL, max_val)
        self.labels[label_index].config(text = dice_roll)

def main():
    DiceRoller().mainloop()

if __name__ == '__main__':
    main()