from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Шаг 1: Зайти на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Шаг 2: Дождаться загрузки картинок явным ожиданием
    third_image = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//img)[3]"))
    )

    # Шаг 3: Получить значение атрибута src у 3-й картинки
    third_image_src = third_image.get_attribute("src")

    # Шаг 4: Выведите значение в консоль 3-й картинки
    print(third_image_src)

finally:
    driver.quit()

