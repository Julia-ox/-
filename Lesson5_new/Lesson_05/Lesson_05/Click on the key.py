from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:

    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        add_button.click()
        time.sleep(1)

    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    print("Количество кнопок 'Delete':", len(delete_buttons))

finally:
    driver.quit()