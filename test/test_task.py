import unittest
from datetime import datetime
from app.task import Task


class TestTask(unittest.TestCase):

    def test_title_assignment(self) -> None:
        title: str = "This is a title"
        content: str = ""
        deadline: datetime = datetime.now()
        task: Task = Task(title, content, deadline)

        self.assertEquals(title, task.get_title())

    def test_content_assignment(self) -> None:
        title: str = ""
        content: str = "This is a task"
        deadline: datetime = datetime.now()
        task: Task = Task(title, content, deadline)

        self.assertEquals(content, task.get_content())

    def test_deadline_assignment(self) -> None:
        title: str = ""
        content: str = ""
        deadline: datetime = datetime.now()
        task: Task = Task(title, content, deadline)

        self.assertEquals(deadline, task.get_deadline())
