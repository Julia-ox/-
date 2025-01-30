from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Шаг 1: Перейдите на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Шаг 2: Нажмите на синюю кнопку
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    # Шаг 3: Получите текст из зеленой плашки
    success_message = driver.find_element(By.ID, "content").text

    # Шаг 4: Выведите его в консоль
    print(success_message)

finally:
    driver.quit()