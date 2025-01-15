# mailing.py

from address import Address

   class Mailing:
       def __init__(self, to_address, from_address, cost, track):
           self.to_address = to_address  # тип данных Address
           self.from_address = from_address  # тип данных Address
           self.cost = cost  # тип данных число
           self.track = track  # тип данных строка

# lesson_3_task_3.py

   from address import Address
   from mailing import Mailing

   # Создаем адреса
   to_addr = Address("101000", "Москва", "Тверская", "1", "10")
   from_addr = Address("121000", "Москва", "Никитская", "2", "5")

   # Создаем экземпляр класса Mailing
   mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=150, track="AB123CD")

   # Печатаем информацию об отправлении
   print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
         f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
         f"в {mailing.to_address.index}, {mailing.to_address.city}, "
         f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
         f"Стоимость {mailing.cost} рублей.")