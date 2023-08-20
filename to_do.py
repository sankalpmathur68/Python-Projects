import tkinter as tk
from tkinter import messagebox
from tkinter import font

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO DO App")
        
        self.tasks = []
        
        self.heading_label = tk.Label(root, text="TO DO App", font=('Helvetica', 20, 'bold'))
        self.heading_label.pack(pady=(10, 0))
        
        self.task_entry = tk.Entry(root, width=30, font=('Helvetica', 14))
        self.task_entry.pack(pady=(10, 0),)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Helvetica', 12))
        self.add_button.pack(pady=(5, 0))
        
        self.task_listbox = tk.Listbox(root, width=40, height=10, font=('Helvetica', 12), selectbackground='#000')
        self.task_listbox.pack(pady=(10, 0), padx=20)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=('Helvetica', 12))
        self.remove_button.pack(pady=(5, 0))
        
        self.quit_button = tk.Button(root, text="Quit", command=root.destroy, font=('Helvetica', 12))
        self.quit_button.pack(pady=(10, 20))
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        
    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.update_task_list()
        
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
