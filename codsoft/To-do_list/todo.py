import json

todo_file = "agenda.json"

def load_todo():
    try:
        with open(todo_file) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_todo(todo):
    with open(todo_file, "w") as f:
        json.dump(todo,f)


def add_task(task):
    todo = load_todo()
    todo.append({"task": task, 
                 "status": "Pending"})
    save_todo(todo)
    print(f"task added {task} ")


def show_task():
    todo = load_todo()
    if not todo:
        print("No task.....")
    else:
        print("\n your task list....")
        for i, t in enumerate(todo, start=1):
            print(f"{i}.{t['task']} - {t['status']}")


def update_task(i, new_task):
    todo = load_todo()
    if 0 < i <= len(todo):
        todo[i-1] = new_task
        save_todo(todo)
        print(f"task updated {new_task}") 
    else:
        print("Invalid task number")

def mark_done(i):
    todo = load_todo()
    if 0 < i <= len(todo):
        todo[i-1]["status"] = "done"
        save_todo(todo)
        print(f"task completed {todo[i-1]}")
    else:
        print("Invalid task number")


def delete_task(i):
    todo = load_todo()
    task = todo.pop(2)
    save_todo(todo)
    print(f"task deleted {task}")


def main():
    while True:
        print("\n To-Do list  Options....")
        print("1. add task")
        print("2. show task")
        print("3. update task")
        print("4. complete task")
        print("5. delete task")
        print("6. exit")

        choice = input("Enter your choice:")

        if choice == "1":
            task = input("Enter new task:")
            add_task(task)

        elif choice == "2":
            show_task()

        elif choice == "3":
            show_task()
            i = int(input("Enter task number:"))
            new_task = input("enter new task:")
            update_task(i , new_task)
             
        elif choice == "4":
            show_task()
            i = int(input("Enter task number:"))
            mark_done(i)

        elif choice == "5":
            show_task()
            i = int(input("Enter task number:"))
            delete_task(i)

        elif choice == "6":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



