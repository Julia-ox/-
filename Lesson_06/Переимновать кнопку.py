from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Шаг 1: Перейти на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Шаг 2: Указать в поле ввода текст "SkyPro"
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Шаг 3: Нажать на синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Шаг 4: Получить текст кнопки
    updated_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "updatingButton"))
    )
    button_text = updated_button.text

    # Шаг 5: Получить текст кнопки в консоль
    print(button_text)

finally:
    # Закройте драйвер
    driver.quit()