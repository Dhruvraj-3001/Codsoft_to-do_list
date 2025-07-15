import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index] = f"✔️ {tasks[index]}"
        update_listbox()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to mark as done.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="To-Do List", font=("Arial", 18, "bold")).pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)

task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
task_listbox.pack(pady=10)

root.mainloop()