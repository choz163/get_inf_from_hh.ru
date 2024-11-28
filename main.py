from src.api import HH
from src.vacancy import Vacancy
from src.file_handler import JSONHandler


def filter_vacancies(vacancies, filter_words):
    filtered = []
    for vacancy in vacancies:
        if any(word.lower() in vacancy.title.lower() for word in filter_words):
            filtered.append(vacancy)
    return filtered


def get_vacancies_by_salary(vacancies, salary_range):
    if "-" not in salary_range:
        print(
            "Неверный формат диапазона зарплат. Используйте формат 'минимум - максимум'."
        )
        return vacancies

    min_salary, max_salary = map(int, salary_range.split("-"))
    return [
        vacancy for vacancy in vacancies if min_salary <= vacancy.salary <= max_salary
    ]


def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda x: x.salary, reverse=True)


def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)


def main():
    json_handler = JSONHandler("vacancies.json")
    hh = HH()
    query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000 - 150000): ")

    try:
        vacancies_data = hh.get_vacancies(query)
        vacancies = [
            Vacancy(
                data["name"],
                data["employer"]["name"],
                (
                    data["salary"]["from"]
                    if data["salary"] and data["salary"]["from"] is not None
                    else 0
                ),
                data["alternate_url"],
            )
            for data in vacancies_data
        ]

        # Применяем фильтрацию и сортировку
        filtered_vacancies = filter_vacancies(vacancies, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

        if top_vacancies:
            print("Топ вакансии:")
            print_vacancies(top_vacancies)

            # Сохраняем отфильтрованные вакансии
            json_handler.add_data(top_vacancies)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
