from app.task import Task
from app.user import User
from datetime import datetime


class Controller:

    user: User

    def get_user_name(self):
        ...

    def change_task_title(self, task_index: int, new_task_title: str) -> None:
        """Raises ValueError if the index isn't in the tasks list."""
        self.user.tasks[task_index].change_title(new_task_title)

    def change_task_content(self, task_index: int, new_task_content: str) -> None:
        """Raises ValueError if the index isn't in the tasks list."""
        self.user.tasks[task_index].change_content(new_task_content)

    def change_task_deadline(self, task_index: int, new_task_deadline: datetime) -> None:
        """Raises ValueError if the index isn't in the tasks list."""
        self.user.tasks[task_index].change_deadline(new_task_deadline)