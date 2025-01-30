from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

##driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

close_button = driver.find_element(By.XPATH, "//div[@id='modal']//button[text()='Close']")
driver.find_element(By.LINK_TEXT, "Close").click()

driver.quit()
