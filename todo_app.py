#todo_application (cli/gui)

import json
import sys
import tkinter as tk
from tkinter import messagebox

#===========================
#STORAGE FUNCTIONS
#===========================

FILE = "todos.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)
        
        
#===========================
#CLI MODE
#===========================

def cli_menu():
    while True:
        print("/n=== TO-DO LIST (CLI MODE) ===")
        print("1. Add Task")
        print("2.View Tasks")
        print("3.Mark Task Done")
        print("4.Delete Task")
        print("5.Exit")

        choice=input("choose an option:")

        tasks = load_tasks()

        if choice == "1":
            task = input("Enter the task:")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks):
                    status = " " if t["done"] else " "
                    print(f"{i+1}. {t["task"]}  [{status}]")

        elif choice == "3":
            num = int(input("Enter task number to mark done: ")) -1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
                save_tasks(tasks)
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            num = int(input("Enter task number to delete: ")) -1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_tasks(tasks)
                print("Task deleted!")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


 #===========================
 # GUI MODE
 # ==========================

def gui_mode():
    tasks = load_tasks()

    def refresh_list():
        listbox.delete(0, tk.END)
        for t in tasks:
            status = " " if t["done"] else " "
            listbox.insert(tk.END, f"{t['task']} [{status}]")

    def add_task():
        task = entry.get()
        if task.strip() == "":
            messagebox.showerror("Error", "Task cannot be empty!")
            return
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        entry.delete(0, tk.END)
        refresh_list()

    def mark_done():
        try:
            index = listbox.curselection()[0]
            tasks[index]["done"] = True
            save_tasks(tasks)
            refresh_list()
        except:
            messagebox.showerror("Error", "Select a task")

    def delete_task():
        try:
            index = listbox.curselection()[0]
            tasks.pop(index)
            save_tasks(tasks)
            refresh_list()
        except:
            messagebox.showerror("Error", "Select a task")

    # GUI Layout
    root = tk.Tk()
    root.title("To-Do List")

    entry = tk.Entry(root, width=35)
    entry.grid(row=0, column=0, padx=10, pady=10)


    add_btn = tk.Button(root, text="Add Task", command=add_task)
    add_btn.grid(row=0,column=1)


    listbox = tk.Listbox(root, width=50, height=10)
    listbox.grid(row=1, column=0, columnspan=2, padx=10)


    done_btn = tk.Button(root, text="Mark Done", command=mark_done)
    done_btn.grid(row=2, column=0, pady=10, sticky="w")


    delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
    delete_btn.grid(row=2, column=1, pady=10, sticky="e")


    refresh_list()
    root.mainloop()


#===========================
# MAIN CONTROLLER
#===========================

if __name__ == "__main__":
    if len(sys.argv) <2:
        print("Usage:")
        print("  python todo_app.py cli  - Run in CLI mode")
        print("  python todo_app.py gui  - Run in GUI mode")
    else:
            mode = sys.argv[1]
            if mode == "cli":
                cli_menu()
            elif mode == "gui":
                gui_mode()
            else:
                print("Invalid mode. Use 'cli' or 'gui'.")





                      

    


