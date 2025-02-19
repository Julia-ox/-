
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculatorPage import calculator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriverManager


def(self):
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


def test_calculation(self):
    # Нажать кнопку 7
    seven_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "class="btn btn-outline-primary"[id='number7']")))
    seven_button.click()

    plus_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[.='+']"))
    )
    plus_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.='+']"))
    )
    plus_button.click()

    eight_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[.='8']"))
    )
    eight_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.='8']"))
    )
    eight_button.click()

    equals_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[.='=']"))
    )
    equals_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.='=']"))
    )
    equals_button.click()

    # Шаг 4: Проверка результата
    result = WebDriverWait(driver, 50).until(  # Ждем до 50 секунд
        EC.text_to_be_present_in_element((By.ID, "result"), "15")

    assert result == True
    driver.quit()