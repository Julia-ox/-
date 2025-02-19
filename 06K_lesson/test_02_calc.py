import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Указываем путь к файлу chromedriver.exe
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем страницу
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

try:
    # Ожидаем появления и вводим значение в поле задержки
    delay_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'delay')))
    delay_input.clear()
    delay_input.send_keys('45')

    # Находим и нажимаем кнопки
    button_7 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='7']")))
    button_plus = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='+']")))
    button_8 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='8']")))
    button_equals = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='=']")))

    button_7.click()
    button_plus.click()
    button_8.click()
    button_equals.click()

    # Ожидаем появления результата и проверяем его
    result = WebDriverWait(driver, 75).until(EC.text_to_be_present_in_element((By.ID, 'result'), '15'))

    assert result == True, "Результат не равен 15"

finally:
    # Закрываем браузер
    driver.quit()