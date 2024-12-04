import requests
from abc import ABC, abstractmethod


class APIClient(ABC):
    @abstractmethod
    def _connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass


class HH(APIClient):
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"text": "", "page": 0, "per_page": 100}
        self._vacancies = []

    def _connect_to_api(self):
        response = requests.get(self._url, headers=self._headers, params=self._params)
        if response.status_code != 200:
            raise Exception(f"Error fetching data: {response.status_code}")
        return response

    def get_vacancies(self, keyword: str):
        self._params["text"] = keyword
        self._params["page"] = 0
        while self._params["page"] < 20:
            response = self._connect_to_api()
            vacancies = response.json().get("items", [])
            if vacancies:
                self._vacancies.extend(vacancies)
                self._params["page"] += 1
            else:
                break
        return self._vacancies
