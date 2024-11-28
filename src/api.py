import requests
from abc import ABC, abstractmethod
from typing import List, Dict

class API(ABC):
    """Абстрактный класс для взаимодействия с API."""

    @abstractmethod
    def connect(self) -> None:
        """Подключение к API."""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получение вакансии через API."""


class HeadHunterAPI(API):
    """Класс для взаимодействия с API hh.ru."""

    def __init__(self):
        self._base_url = "https://api.hh.ru/vacancies"
        self._connected = False

    def connect(self) -> None:
        """Подключение к API."""
        self._connected = True

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получение вакансии через API."""
        if not self._connected:
            self.connect()

        params = {"text": keyword, "per_page": 100}
        response = requests.get(self._base_url, params=params)
        response.raise_for_status()
        return response.json()["items"]
