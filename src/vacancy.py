class Vacancy:
    __slots__ = ["title", "company", "salary", "link"]

    def __init__(self, title: str, company: str, salary: int, link: str):
        self.title = self._validate_string(title)
        self.company = self._validate_string(company)
        self.salary = self._validate_salary(salary)
        self.link = self._validate_string(link)

    def _validate_string(self, value: str) -> str:
        if not value:
            raise ValueError("Строковое значение не может быть пустым")
        return value

    def _validate_salary(self, value: int) -> int:
        if value < 0:
            return 0
        return value

    def __repr__(self):
        return f"Vacancy(title={self.title}, company={self.company}, salary={self.salary}, link={self.link})"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary
