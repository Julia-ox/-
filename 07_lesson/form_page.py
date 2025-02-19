from .MainPage import BasePage
from selenium.webdriver.common.by import By
import pytest

class FormPage(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    ADDRESS_INPUT = (By.ID, 'address')
    EMAIL_INPUT = (By.ID, 'email')
    PHONE_NUMBER_INPUT = (By.ID, 'phoneNumber')
    ZIP_CODE_INPUT = (By.ID, 'zipCode')
    CITY_INPUT = (By.ID, 'city')
    COUNTRY_INPUT = (By.ID, 'country')
    JOB_POSITION_SELECT = (By.ID, 'jobPosition')
    COMPANY_INPUT = (By.ID, 'company')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Submit"]')

    SUCCESS_COLOR = 'rgba(0, 128, 0, 1)'
    ERROR_COLOR = 'rgba(255, 0, 0, 1)'

    def open(self):
        self.driver.get(self.URL)

    def fill_first_name(self, first_name):
        element = self.find_element(self.FIRST_NAME_INPUT)
        element.clear()
        element.send_keys(first_name)

    def fill_last_name(self, last_name):
        element = self.find_element(self.LAST_NAME_INPUT)
        element.clear()
        element.send_keys(last_name)

    def fill_address(self, address):
        element = self.find_element(self.ADDRESS_INPUT)
        element.clear()
        element.send_keys(address)

    def fill_email(self, email):
        element = self.find_element(self.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)

    def fill_phone_number(self, phone_number):
        element = self.find_element(self.PHONE_NUMBER_INPUT)
        element.clear()
        element.send_keys(phone_number)

    def fill_zip_code(self, zip_code):
        element = self.find_element(self.ZIP_CODE_INPUT)
        element.clear()
        element.send_keys(zip_code)

    def fill_city(self, city):
        element = self.find_element(self.CITY_INPUT)
        element.clear()
        element.send_keys(city)

    def select_country(self, country):
        element = self.find_element(self.COUNTRY_INPUT)
        element.click()
        options = element.find_elements(By.TAG_NAME, 'option')
        for option in options:
            if option.text == country:
                option.click()
                break

    def select_job_position(self, job_position):
        element = self.find_element(self.JOB_POSITION_SELECT)
        element.click()
        options = element.find_elements(By.TAG_NAME, 'option')
        for option in options:
            if option.text == job_position:
                option.click()
                break

    def fill_company(self, company):
        element = self.find_element(self.COMPANY_INPUT)
        element.clear()
        element.send_keys(company)

    def submit_form(self):
        button = self.find_element(self.SUBMIT_BUTTON)
        button.click()

    def get_color_of_input(self, input_locator):
        element = self.find_element(input_locator)
        return element.value_of_css_property('border-color')