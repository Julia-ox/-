from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.XPATH, "//input[@type='number']")

    # Вводим значение 1000
    input_field.send_keys("1000")
    sleep(1)  

    # Очищаем поле
    input_field.clear()
    sleep(1)

    # Вводим значение 999
    input_field.send_keys("999")
    sleep(1)

finally:
    # Закрываем браузер
    driver.quit()