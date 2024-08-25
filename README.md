# To-Do List Application

## Description

This application allows users to manage their to-do list. Users can add, delete, and mark tasks as completed. Tasks are saved in a JSON file to be accessible upon the next program launch.

## Requirements

- Python 3.x
- Packages: `json`, `os` (included in Python's standard library)

## Installation and Running

### Installation

1. Download the project from the repository or copy the files to your local environment.
2. Ensure Python is installed (if not already).

### Running

1. Navigate to the project directory in the command line or terminal.
2. Run the `main.py` file with the command:
   ```bash
   python main.py

Usage
Menu Options
The program offers the following options:

Add Task: Add a new task.

Enter the task title.
Enter the task description (optional).
Delete Task: Delete a task.

Enter the task number you wish to delete.
Mark Task as Completed: Mark a task as completed.

Enter the task number you wish to mark as completed.
Show Tasks: Display all tasks.

Lists all tasks with their completion status.
Exit: Exit the program.

Usage Example
Adding a Task:
Choose an option: 1
Enter task title: Finish report
Enter task description: Complete the financial report for Q2

Deleting a Task:
Choose an option: 2
Enter task number to delete: 1

Marking a Task as Completed:
Choose an option: 3
Enter task number to mark as completed: 1

Showing Tasks:
Choose an option: 4
1. Finish report: Complete the financial report for Q2 [✔]

Exiting the Program:
Choose an option: 5


Classes and Methods
Task Class
Attributes:

title (str): The title of the task.
description (str): The description of the task (optional).
completed (bool): The completion status of the task (default is False).
Methods:

__init__(self, title, description=""): Initializes the class.
__str__(self): Returns a string representation of the task.
TodoList Class
Attributes:

filename (str): The name of the file for saving tasks (default is "tasks.json").
tasks (list): A list of Task objects.
Methods:

__init__(self, filename="tasks.json"): Initializes the class.
load_tasks(self): Loads tasks from the file.
save_tasks(self): Saves tasks to the file.
add_task(self, task): Adds a task to the list.
delete_task(self, index): Deletes a task by index.
mark_task_completed(self, index): Marks a task as completed.
Additional Notes
The program automatically saves changes to the tasks.json file, which is used for storing tasks.
The program does not ask for confirmation before deleting a task.
Authors
[Vladyslav Stelmakh]
