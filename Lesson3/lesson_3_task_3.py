from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "12")

# Создаем почтовое отправление
mailing = Mailing(to_address, from_address, 100, "ABC123456789")

# Выводим информацию о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment} "
      f"в {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")