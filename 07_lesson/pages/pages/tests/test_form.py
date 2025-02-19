from selenium.webdriver.common.by import By
from pages.MainPage import MainPage
def:
    browser = webdriver.Chrome() #Открываем браузер
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
    main_page.set_cookie_policy()


#@pytest.mark.usefixtures('setup')
#class TestForm:
    #def test_submit_form_with_empty_zip_code(self):
        page = FormPage(self.driver)
        page.open()

        # Заполнение формы
        page.fill_first_name("Иван")
        page.fill_last_name("Петров")
        page.fill_address("Ленина, 55-3")
        page.fill_email("test@skypro.com")
        page.fill_phone_number("+7985899998787")
        page.fill_zip_code("")
        page.fill_city("Москва")
        page.select_country("Россия")
        page.select_job_position("QA")
        page.fill_company("SkyPro")

        # Отправка формы
        page.submit_form()

        # Проверки
        assert page.get_color_of_input(page.ZIP_CODE_INPUT) == page.ERROR_COLOR

        fields_to_check = [
            page.FIRST_NAME_INPUT,
            page.LAST_NAME_INPUT,
            page.ADDRESS_INPUT,
            page.EMAIL_INPUT,
            page.PHONE_NUMBER_INPUT,
            page.CITY_INPUT,
            page.COUNTRY_INPUT,
            page.JOB_POSITION_SELECT,
            page.COMPANY_INPUT
        ]

        for field in fields_to_check:
            assert page.get_color_of_input(field) == page.SUCCESS_COLOR