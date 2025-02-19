from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )


class CalculatorPage(BasePage):
    # Локаторы элементов
    _INPUT_DELAY_LOCATOR = (By.ID, 'delay')
    _BUTTON_7_LOCATOR = (By.CSS_SELECTOR, '#seven')
    _BUTTON_PLUS_LOCATOR = (By.CSS_SELECTOR, '#plus')
    _BUTTON_8_LOCATOR = (By.CSS_SELECTOR, '#eight')
    _BUTTON_EQUALS_LOCATOR = (By.CSS_SELECTOR, '#equals')
    _RESULT_LOCATOR = (By.CSS_SELECTOR, '.display')

    # Методы для взаимодействия с элементами
    def set_delay(self, delay_value):
        input_delay = self.find_element(*self._INPUT_DELAY_LOCATOR)
        input_delay.clear()
        input_delay.send_keys(delay_value)

    def click_button_7(self):
        button_7 = self.find_element(*self._BUTTON_7_LOCATOR)
        button_7.click()

    def click_button_plus(self):
        button_plus = self.find_element(*self._BUTTON_PLUS_LOCATOR)
        button_plus.click()

    def click_button_8(self):
        button_8 = self.find_element(*self._BUTTON_8_LOCATOR)
        button_8.click()

    def click_button_equals(self):
        button_equals = self.find_element(*self._BUTTON_EQUALS_LOCATOR)
        button_equals.click()

    def get_result(self):
        result_display = self.find_element(*self._RESULT_LOCATOR)
        return result_display.text