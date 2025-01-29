from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(3)

driver.quit()