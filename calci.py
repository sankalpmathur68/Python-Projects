import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=('Helvetica', 24), bd=10, insertwidth=4, width=15, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
       
        self.create_buttons()
        
    def create_buttons(self):
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('!', 5, 2),
        ]
        
        for (text, row, col) in button_texts:
            button = tk.Button(self.root, text=text, font=('Helvetica', 18, 'bold'), padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#000")
            button.grid(row=row, column=col, padx=5, pady=5)
        
    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry_var.get())
                self.entry_var.set(result)
                # self.history += f"{self.entry_var.get()} = {result}\n"
                # self.history_var.set(self.history)
            except Exception:
                self.entry_var.set("Error")
        elif text == "C":
            self.entry_var.set("")
        elif text == "√":
            try:
                value = float(self.entry_var.get())
                result = math.sqrt(value)
                self.entry_var.set(result)
            except Exception:
                self.entry_var.set("Error")
        elif text == "!":
            try:
                value = int(self.entry_var.get())
                result = math.factorial(value)
                self.entry_var.set(result)
            except Exception:
                self.entry_var.set("Error")
        else:
            current_text = self.entry_var.get()
            self.entry_var.set(current_text + text)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
