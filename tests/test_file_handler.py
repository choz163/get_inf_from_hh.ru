import pytest
from src.file_handler import JSONHandler
from unittest.mock import patch


@pytest.fixture
def mock_get_data():
    with patch("src.file_handler.JSONHandler.get_data") as mock:
        mock.return_value = [
            {
                "title": "Python Developer",
                "company": "Google",
                "salary": 100000,
                "link": "https://example.com",
            }
        ]
        yield mock


@pytest.fixture
def mock_add_data():
    with patch("src.file_handler.JSONHandler.add_data") as mock:
        mock.return_value = None
        yield mock


def test_get_data(mock_get_data):
    json_handler = JSONHandler("vacancies.json")
    vacancies = json_handler.get_data()
    assert vacancies


def test_add_data(mock_add_data):
    json_handler = JSONHandler("vacancies.json")
    vacancies = [
        {
            "title": "Python Developer",
            "company": "Google",
            "salary": 100000,
            "link": "https://example.com",
        }
    ]
    json_handler.add_data(vacancies)
