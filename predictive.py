import tkinter as tk
from tkinter import ttk

class PredictiveTypingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("EMPLOYEES NAMES WORKED IN TCS")
        self.entry = tk.Entry(self.root, width=100)
        self.entry.pack()
        self.predictions = tk.Listbox(self.root)
        self.predictions.pack()
        self.update_predictions()

    def update_predictions(self):
        text = self.entry.get()
        predictions = self.predict(text)
        self.predictions.delete(0, tk.END)
        for prediction in predictions:
            self.predictions.insert(tk.END, prediction)
        self.root.after(300, self.update_predictions)

    def predict(self, text):
        # This is a simple prediction system that suggests words based on the input
        words = ["anal","bobby", "cherry", "dathu", "elderberry","first","ghloe" , "hydney","iackenzie","ink","jeyton","kaegan","lasmine","MorgLauAlexis","nayla","oudin","peter","qailey","rulia","sadie","trooklyn","uddison","vubrey","wrielle","ynna"]
        return [word for word in words if word.startswith(text)]

root = tk.Tk()
system = PredictiveTypingSystem(root)
root.mainloop()
