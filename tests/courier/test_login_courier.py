import allure
from faker import Faker
from data import LOG_FIELD_NOT_FOUND_MESSAGE, LOG_WRONG_CREDS_MESSAGE


class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    @allure.description("Тест проверяет успешный логин курьера с валидными данными, указанными при регистрации.")
    def test_login_user_success(self, courier_methods, courier_data):
        login = courier_data[0]
        password = courier_data[1]

        payload = {
            'login': login,
            'password': password
        }
        response = courier_methods.login_courier(payload)

        assert response.status_code == 200 and 'id' in response.json()

    @allure.title("Логин с отсутствующим полем")
    @allure.description("Тест проверяет логин курьера с отсутствующим обязательным полем - логин.")
    def test_login_with_missing_field(self, courier_methods, courier_data):
        password = courier_data[1]

        payload = {
            'password': password
        }
        response = courier_methods.login_courier(payload)

        assert response.status_code == 400 and response.json()['message'] == LOG_FIELD_NOT_FOUND_MESSAGE

    @allure.title("Логин с несуществующими учетными данными")
    @allure.description("Тест проверяет логин курьера с несуществующими учетными данными.")
    def test_login_with_wrong_credentials(self, courier_methods):
        fake = Faker()
        payload = {
            'login': fake.user_name(),
            'password': fake.password()
        }
        response = courier_methods.login_courier(payload)

        assert response.status_code == 404 and response.json()['message'] == LOG_WRONG_CREDS_MESSAGE
