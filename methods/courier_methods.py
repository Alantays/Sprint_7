import allure
import requests
from data import BASE_URL, COURIERS_URL


class CourierMethods:

    @allure.step("Создание курьера с указанными параметрами")
    def create_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=payload)
        return response

    @allure.step("Удаление курьера по ID")
    def delete_courier(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{id}')
        return response

    @allure.step("Аутентификация курьера с параметрами")
    def login_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=payload)
        return response
