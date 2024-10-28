import allure
from data import DUP_LOGIN_MESSAGE, REQ_FIELD_NOT_FOUND_MESSAGE
from faker import Faker


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Тест проверяет успешное создание курьера с корректными данными.")
    def test_create_courier_success(self, courier_methods, courier_data):
        response = courier_data[4]

        assert response.status_code == 201 and response.json()['ok'] is True

    @allure.title("Попытка создания дубликата курьера")
    @allure.description("Тест проверяет создание курьера с логином, который уже зарегистрирован в системе.")
    def test_create_duplicate_courier(self, courier_methods, courier_data):
        login = courier_data[0]
        password = courier_data[1]
        first_name = courier_data[2]

        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        response = courier_methods.create_courier(payload)

        assert response.status_code == 409 and response.json()['message'] == DUP_LOGIN_MESSAGE

    @allure.title("Создание курьера с отсутствующим обязательным полем")
    @allure.description("Тест проверяет создание курьера с отсутствующим обязательным полем - пароль.")
    def test_create_courier_with_missing_required_field(self, courier_methods):
        fake = Faker()
        payload = {
            'login': fake.user_name(),
            'firstName': fake.first_name()
        }
        response = courier_methods.create_courier(payload)

        assert response.status_code == 400 and response.json()['message'] == REQ_FIELD_NOT_FOUND_MESSAGE
