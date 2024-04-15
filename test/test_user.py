from app.user import User
from app.user import Task
from datetime import datetime
import unittest

class TestUser(unittest.TestCase):

    def test_add_task_passing_task_object(self) -> None:
        user: User = User("Testing user")
        task: Task = Task("Test title", "Test content", datetime.now())
        user.add_task(task)

        self.assertEquals(task, user.tasks[-1])

    def test_add_task_passing_task_arguments(self) -> None:

        # This test is failing for some reason.

        user: User = User("Testing user")
        expected_date = datetime.now()
        expected_task: Task = Task("Test title", "Test content", expected_date)
        user.add_task("Test title", "Test content", expected_date)

        print(expected_task)
        print(user.tasks[-1])

        self.assertEquals(expected_task, user.tasks[-1])
