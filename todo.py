import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_var = tk.StringVar()

        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def mark_completed(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            messagebox.showinfo("Completed", f"Task '{task}' marked as completed!")
        else:
            messagebox.showwarning("Warning", "Please select a task!")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            messagebox.showinfo("Deleted", f"Task '{task}' deleted!")
        else:
            messagebox.showwarning("Warning", "Please select a task!")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
