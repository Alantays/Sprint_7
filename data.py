BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

DUP_LOGIN_MESSAGE = 'Этот логин уже используется. Попробуйте другой.'
REQ_FIELD_NOT_FOUND_MESSAGE = 'Недостаточно данных для создания учетной записи'
LOG_FIELD_NOT_FOUND_MESSAGE = 'Недостаточно данных для входа'
LOG_WRONG_CREDS_MESSAGE = 'Учетная запись не найдена'

ORDER_DATA_1 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "ул. Ленина, 123",
    "metroStation": 4,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-26",
    "comment": "И побыстрее"
}

ORDER_DATA_2 = {
    "firstName": "Василий",
    "lastName": "Васильев",
    "address": "ул. Пушкина, 456",
    "metroStation": 5,
    "phone": "+7 800 555 35 36",
    "rentTime": 3,
    "deliveryDate": "2020-07-27",
    "comment": "И помедленнее",
    "color": ["BLACK"]
}

ORDER_DATA_3 = {
    "firstName": "Петр",
    "lastName": "Петров",
    "address": "ул. Лермонтова, 789",
    "metroStation": 6,
    "phone": "+7 800 555 35 37",
    "rentTime": 7,
    "deliveryDate": "2020-08-28",
    "comment": "Без комментариев",
    "color": ["GREY"]
}

ORDER_DATA_4 = {
    "firstName": "Алексей",
    "lastName": "Алексеев",
    "address": "ул. Гоголя, 1011",
    "metroStation": 7,
    "phone": "+7 800 555 35 38",
    "rentTime": 4,
    "deliveryDate": "2020-09-29",
    "comment": "Спасибо",
    "color": ["GREY", "BLACK"]
}