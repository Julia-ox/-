from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    # Локаторы элементов
    _input_delay_locator = (By.ID, 'delay')
    _button_7_locator = (By.CSS_SELECTOR, "#seven")
    _button_plus_locator = (By.CSS_SELECTOR, "#plus")
    _button_8_locator = (By.CSS_SELECTOR, "#eight")
    _button_equals_locator = (By.CSS_SELECTOR, "#equals")
    _result_locator = (By.CSS_SELECTOR, ".display")

    # Метод для ожидания появления элемента
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    # Метод для ввода значения задержки
    def set_delay(self, delay_value):
        self.wait_for_element(self._input_delay_locator)
        input_delay = self.driver.find_element(*self._input_delay_locator)
        input_delay.clear()
        input_delay.send_keys(delay_value)

    # Метод для нажатия кнопки 7
    def click_button_7(self):
        self.wait_for_element(self._button_7_locator)
        button_7 = self.driver.find_element(*self._button_7_locator)
        button_7.click()

    # Метод для нажатия кнопки +
    def click_button_plus(self):
        self.wait_for_element(self._button_plus_locator)
        button_plus = self.driver.find_element(*self._button_plus_locator)
        button_plus.click()

    # Метод для нажатия кнопки 8
    def click_button_8(self):
        self.wait_for_element(self._button_8_locator)
        button_8 = self.driver.find_element(*self._button_8_locator)
        button_8.click()

    # Метод для нажатия кнопки =
    def click_button_equals(self):
        self.wait_for_element(self._button_equals_locator)
        button_equals = self.driver.find_element(*self._button_equals_locator)
        button_equals.click()

    # Метод для получения результата
    def get_result(self):
        self.wait_for_element(self._result_locator)
        result_display = self.driver.find_element(*self._result_locator)
        return result_display.text