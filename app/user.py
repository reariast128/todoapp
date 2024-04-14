from datetime import datetime, timedelta
from functools import singledispatchmethod
from app.task import Task
from typing import List


class User:

    name: str
    tasks: List[Task]

    def __init__(self, name) -> None:
        self.name = name
        self.tasks = list()

        # Set the defaults' task values

        _default_task_title: str = f"First's {self.name} Task!"
        _default_task_content: str = ""
        _default_task_deadline: datetime = datetime.now() + timedelta(days=7)

        # Creating the default task

        default_task: Task = Task(
            _default_task_title, _default_task_content, _default_task_deadline)

        self.tasks.append(default_task)

    @singledispatchmethod
    def add_task(self):
        """Add a task by passing as an argument a Task object or task_title, task_content, and task_deadline as arguments.
        
        task: Task,
        
        task_title: str,
        task_content: str,
        task_deadline: datetime
        
        """
        raise NotImplementedError("Cant add this task.")

    @add_task.register
    def _(self, task: Task) -> None:
        self.tasks.append(task)

    @add_task.register
    def _(self, task_title: str, task_content: str, task_deadline: datetime) -> None:
        """Raises ValueError if the index isn't in the tasks list."""
        self.tasks.append(Task(task_title, task_content, task_deadline))

    def delete_task(self, task_index: int) -> None:
        """Removes a task using it's index.

        Raises ValueError if the index isn't in the tasks list.
        """
        self.tasks.pop(task_index)