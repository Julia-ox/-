def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    :param year: Год (число)
    :return: True, если год високосный, иначе False
    """
    return year % 4 == 0

# Пример использования
year = 2024  # Замените на любой год
result = is_year_leap(year)
print(f"Год {year}: {result}")
