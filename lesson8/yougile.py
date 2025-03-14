import requests
from settings import LOGIN, PASSWORD, COMPANY_ID
import os

class Yougile:
    def __init__(self):
        os.environ['YOUGILE_TOKEN'] = '998'

    def some_method(self):
        pass


class Yougile:
    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD
        self.company_id = COMPANY_ID
        self.url = "https://ru.yougile.com/api-v2/auth/keys"
    def get_auth_key(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

