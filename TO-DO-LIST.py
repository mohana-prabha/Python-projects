#TO-DO-LIST

import json
import os


class ToDoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks =[]
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks,file)

    def add_task(self, task):
        self.tasks.append({"task": task,"completed": False})
        self.save_tasks()
        
    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!\n")
            return
        print("\nYour TO-DO LIST:")
        for i, task in enumerate(self.tasks, 1):
            status="Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} --> {status}")
            print()

    def mark_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number -1][completed]=True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks.pop(task_number -1)
            self.save_tasks()
            print("Task deleted!")
        else:
            print("Invalid task number!")

def main():
    todo= ToDoList()

    while True:
        print("\n-----To-Do-List MENU -----")
        print("1.ADD TASK")
        print("2.SHOW TASKS")
        print("3.MARK TASK AS DONE")
        print("4.DELETE TASK")
        print("5.EXIT")

        choice=input("Enter your choice (1-5): ")

        if choice=="1":
            task=input("Enter the task: ")
            todo.add_task(task)
            print("Task added successfully!")

        elif choice=="2":
            todo.show_tasks()

        elif choice=="3":
            todo.show_tasks()
            num=int(input("Enter the task number to mark as completed: "))
            todo.mark_done(num)

        elif choice=="4":
            todo.show_tasks()
            num=int(input("Enter the task number to delete: "))
            todo.delete_task(num)

        elif choice=="5":
            print("Goodbye!")
            break

        if __name__ == "__main__":
            main()
            
                              
