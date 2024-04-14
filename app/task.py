from datetime import datetime


class Task:
    _created_time: datetime
    _modified_time: datetime
    _deadline: datetime
    _title: str
    _content: str

    def __init__(self, title: str, content: str, deadline: datetime) -> None:
        self._created_time = datetime.now()
        self._modified_time = datetime.now()
        self._title = title
        self._content = content
        self._deadline = deadline

    def __str__(self) -> str:
        return f"{self._title}, created at {self._created_time.strftime('%c')}"

    def change_content(self, new_content: str) -> None:
        self._content = new_content
        self._modified_time = datetime.now()

    def change_deadline(self, new_deadline: datetime) -> None:
        self._deadline = new_deadline
        self._modified_time = datetime.now()

    def change_title(self, new_title: str) -> None:
        self._title = new_title
        self._modified_time = datetime.now()

    def get_content(self) -> str:
        return self._content

    def get_created_date(self) -> datetime:
        return self._created_time

    def get_deadline(self) -> datetime:
        return self._deadline

    def get_modified_date(self) -> datetime:
        return self._modified_time

    def get_title(self) -> str:
        return self._title
