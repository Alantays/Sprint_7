import pytest
from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4
import allure


class TestCreateOrder:

    @allure.title("Тест на создание заказа с различными данными")
    @allure.description("Проверка создания заказа с различными наборами данных")
    @pytest.mark.parametrize('order_data', [
        ORDER_DATA_1,
        ORDER_DATA_2,
        ORDER_DATA_3,
        ORDER_DATA_4
    ])
    def test_create_order_with_various_data(self, order_data, order_methods):
        with allure.step(f"Создание заказа с данными: {order_data}"):
            status_code, response_json = order_methods.post_order(order_data)

        assert status_code == 201 and 'track' in response_json
