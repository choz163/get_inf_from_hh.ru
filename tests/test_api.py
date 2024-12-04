import pytest
from src.api import HH
from unittest.mock import patch


@pytest.fixture
def mock_get_vacancies():
    with patch("src.api.HH.get_vacancies") as mock:
        mock.return_value = [
            {
                "name": "Python Developer",
                "employer": {"name": "Google"},
                "salary": {"from": 100000},
                "alternate_url": "https://example.com",
            }
        ]
        yield mock


def test_get_vacancies(mock_get_vacancies):
    hh = HH()
    vacancies = hh.get_vacancies("Python")
    assert vacancies
