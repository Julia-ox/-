# user.py

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")


# lesson_3_task_1.py

from User import User

# Создаем экземпляр User
my_user = User("Иван", "Иванов")

# Вызываем методы у объекта my_user
my_user.print_first_name()  # Печатает имя
my_user.print_last_name()  # Печатает фамилию
my_user.print_full_name()  # Печатает полное имя