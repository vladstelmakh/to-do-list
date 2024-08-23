
import json
import os

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✔" if self.completed else "✖"
        return f"{self.title}: {self.description} [{status}]"

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()  # Завантаження завдань при запуску

    def load_tasks(self):
        if os.path.exists(self.filename):  # Перевірка наявності файлу
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)  # Завантаження даних із JSON-файлу
                return [Task(**task) for task in tasks_data]  # Створення об'єктів Task
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)  # Збереження завдань у файл

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()  # Збереження завдань після додавання

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()  # Збереження завдань після видалення

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()  # Збереження завдань після зміни статусу
