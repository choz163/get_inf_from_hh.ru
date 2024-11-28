from typing import Union

class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("_name", "_url", "_salary", "_description")

    def __init__(self, name: str, url: str, salary: Union[str, int], description: str):
        self._name = name
        self._url = url
        self._salary = self._validate_salary(salary)
        self._description = description

    def _validate_salary(self, salary: Union[str, int]) -> int:
        if isinstance(salary, int):
            return salary
        elif isinstance(salary, str):
            if salary.isdigit():
                return int(salary)
            else:
                return 0
        else:
            raise ValueError("Неверный тип зарплаты")

    def __eq__(self, other: "Vacancy") -> bool:
        return self._salary == other._salary

    def __lt__(self, other: "Vacancy") -> bool:
        return self._salary < other._salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self._salary > other._salary

    def __repr__(self) -> str:
        return f"Вакансия(name={self._name}, url={self._url}, salary={self._salary}, description={self._description})"
