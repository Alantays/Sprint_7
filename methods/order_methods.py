from data import BASE_URL, ORDERS_URL
import requests
import allure


class OrderMethods:

    @allure.step("Отправка заказа с указанными параметрами")
    def post_order(self, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=params)
        return response.status_code, response.json()

    @allure.step("Получение списка заказов")
    def get_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()