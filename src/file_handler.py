import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileHandler(ABC):

    @abstractmethod
    def get_data(self) -> list:
        pass

    @abstractmethod
    def add_data(self, data: list):
        pass

    @abstractmethod
    def remove_data(self):
        pass


class JSONHandler(FileHandler):
    def __init__(self, filename: str = "vacancies.json"):
        self._filename = filename

    def get_data(self) -> list:
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Vacancy(**v) for v in data]
        except FileNotFoundError:
            return []

    def add_data(self, vacancies: list):
        current_data = self.get_data()
        current_titles = {v.title for v in current_data}
        new_data = [v for v in vacancies if v.title not in current_titles]
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(
                [v.__dict__ for v in current_data + new_data],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def remove_data(self):
        with open(self._filename, "w", encoding="utf-8") as file:
            file.truncate(0)
