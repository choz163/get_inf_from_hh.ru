from src.vacancy import Vacancy


def test_validate_string():
    vacancy = Vacancy("Python Developer", "Google", 100000, "https://example.com")
    assert vacancy.title == "Python Developer"


def test_validate_salary():
    vacancy = Vacancy("Python Developer", "Google", 100000, "https://example.com")
    assert vacancy.salary == 100000
