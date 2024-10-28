import allure


class TestGetOrders:
    @allure.title("Тест на получение всех заказов")
    @allure.description("Проверка получения списка всех заказов")
    def test_get_orders(self, order_methods):
        status_code, response_json = order_methods.get_orders()

        assert status_code == 200 and 'orders' in response_json
