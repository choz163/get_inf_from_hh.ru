class Vacancy:
    __slots__ = ["title", "company", "salary", "link"]

    def __init__(self, title: str, company: str, salary: int, link: str):
        self.title = self._non_empty_string_validator(title)
        self.company = self._non_empty_string_validator(company)
        self.salary = self._non_empty_string_validator(salary)
        self.link = self._non_empty_string_validator(link)

    def _non_empty_string_validator(self, value: str) -> str:
        if not value:
            raise ValueError("Строковое значение не может быть пустым")
        return value

    def validate_salary(value: int) -> int:
        """Проверяет, что зарплата неотрицательная."""
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        return value

    def __repr__(self):
        return f"Vacancy(title={self.title}, company={self.company}, salary={self.salary}, link={self.link})"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary
