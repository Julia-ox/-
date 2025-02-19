from selenium.webdriver.common.by import By
class MainPage:
# Метод
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_cookie_policy(self): # Объект cookie берем из спагетти-кода
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)