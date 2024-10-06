class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Неверный индекс задачи")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if not current_tasks:
            print("Все задачи выполнены")
        else:
            for task in current_tasks:
                print(task)

task_manager = TaskManager()

task_manager.add_task("Купить продукты", "2024-10-10")
task_manager.add_task("Сдать проект", "2024-10-07")

task_manager.mark_task_completed(0)

task_manager.show_current_tasks()
