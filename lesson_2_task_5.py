def month_to_season(month):
    # Проверяем номер месяца и возвращаем соответствующий сезон
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный номер месяца"  # Возвращаем сообщение об ошибке, если месяц не в пределах от 1 до 12
month = 2
season = month_to_season(month)
print(f"Месяц {month} относится к сезону: {season}")