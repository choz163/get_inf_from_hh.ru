def validate_string(value: str) -> str:
    """Проверяет, что строка не является пустой."""
    if not value:
        raise ValueError("Строковое значение не может быть пустым")
    return value


def validate_salary(value: int) -> int:
    """Проверяет, что зарплата неотрицательная."""
    if value < 0:
        raise ValueError("Зарплата не может быть отрицательной")
    return value
