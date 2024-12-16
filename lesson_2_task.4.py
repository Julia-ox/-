def fizz_buzz(n):
    """
    Печатает числа от 1 до n с заменой:
    - на 'Fizz', если число делится на 3;
    - на 'Buzz', если число делится на 5;
    - на 'FizzBuzz', если число делится на 3 и на 5.

    :param n: Верхняя граница диапазона (включительно)
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Пример использования
fizz_buzz(17)