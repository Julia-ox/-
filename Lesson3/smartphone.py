class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

        from smartphone import Smartphone

        # Объявляем каталог как список
        catalog = [
            Smartphone("Apple", "iPhone 14", "+79012345678"),
            Smartphone("Samsung", "Galaxy S22", "+79098765432"),
            Smartphone("Google", "Pixel 6", "+79123456789"),
            Smartphone("OnePlus", "9 Pro", "+79234567890"),
            Smartphone("Xiaomi", "Mi 11", "+79345678901")
        ]

        # Цикл для печати каталога
        for smartphone in catalog:
            print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")