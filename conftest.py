import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
import random
import string

@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def courier_data(courier_methods):
    # Генерация случайных значений для логина, пароля и имени
    def generate_random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = courier_methods.create_courier(payload)

    if response.status_code == 201:
        courier_id = response.json().get("id")

    yield [login, password, first_name, courier_id, response]

    courier_methods.delete_courier(courier_id)
