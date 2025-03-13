import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from calculatorPage import CalculatorPage


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.calculator_page = CalculatorPage(self.driver)
        self.driver.get("http://example.com/calculator")  # Укажите URL страницы калькулятора

    def test_calculation(self):
        # Настройка задержки
        self.calculator_page.set_delay(2)

        # Выполнение вычисления "7 + 8"
        self.calculator_page.click_button_7()
        self.calculator_page.click_button_plus()
        self.calculator_page.click_button_8()
        self.calculator_page.click_button_equals()

        # Получение и проверка результата
        result = self.calculator_page.get_result()
        self.assertEqual(result, "15")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()