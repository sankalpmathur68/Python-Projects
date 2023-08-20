import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        self.title_label = tk.Label(root,   text="Password Generator", font=('Helvetica', 20, 'bold'))
        self.title_label.grid(row=0, column=1, padx=50)
        
        self.username_label = tk.Label(root, text="Enter User Name:", font=('Helvetica', 12))
        self.username_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.username_entry = tk.Entry(root, font=('Helvetica', 12))
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.password_length_label = tk.Label(root, text="Enter Password Length:", font=('Helvetica', 12))
        self.password_length_label.grid(row=2, column=0,  padx=10, pady=5)
        
        self.password_length_entry = tk.Entry(root, font=('Helvetica', 12))
        self.password_length_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=('Helvetica', 12))
        self.generate_button.grid(row=3, column=1, padx=10, pady=10)
        
        self.generated_password_label = tk.Label(root, text="", font=('Helvetica', 14), wraplength=300)
        self.generated_password_label.grid(row=4, column=1, padx=10, pady=20)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields, font=('Helvetica', 12))
        self.reset_button.grid(row=5, column=1, padx=10, pady=10)
        
        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password, font=('Helvetica', 12))
        self.accept_button.grid(row=6, column=1, padx=10, pady=10)
        
    def generate_password(self):
        password_length = int(self.password_length_entry.get())
        
        if password_length <= 0:
            self.generated_password_label.config(text="Invalid Password Length")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        
        self.generated_password_label.config(text=generated_password)
    
    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_length_entry.delete(0, tk.END)
        self.generated_password_label.config(text="")
    
    def accept_password(self):
        username = self.username_entry.get()
        generated_password = self.generated_password_label.cget("text")
        if username and generated_password:
            print(f"Username: {username}")
            print(f"Generated Password: {generated_password}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
