# add_task.py
def add_task(task_list, task):
    task_list.append(task)
    return task_list

if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Complete XP Lab Task 2")
    print("Tasks:", tasks)
