from selenium import webdriver

# Указываем путь к файлу chromedriver.exe
driver = webdriver.Chrome(executable_path='C:\Users\Kozlo\Downloads\chromedriver-win64\chromedriver-win64')

# Получаем версию ChromeDriver
print(driver.capabilities['chrome']['chromedriverVersion'])

# Закрываем браузер
driver.quit()