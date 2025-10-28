# view_task.py

def view_tasks(tasks):
    """
    Displays all tasks in a list format.
    If no tasks exist, returns a message.
    """
    if not tasks:
        return "No tasks available."
    
    print("---- Task List ----")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
    return "Tasks displayed successfully."


# Example usage (you can delete this part later if needed)
if __name__ == "__main__":
    task_list = ["Complete XP Lab", "Write unit tests", "Review code"]
    view_tasks(task_list)
