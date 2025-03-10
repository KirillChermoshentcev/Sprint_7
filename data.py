from faker import Faker

faker = Faker()


class TestData:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    NEW_COURIER_URL ='https://qa-scooter.praktikum-services.ru/api/v1/courier'
    LOGIN_COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    CREATE_ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    GET_ORDER_LIST = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    DELETE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/:id'


class ResponseTexts:

    SUCCESSFUL_CREATION = '{"ok":true}'
    LOGIN_ALREADY_USED_ERROR = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    NOT_ENOUGH_DATA_ERROR = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    NOT_ENOUGH_DATA_FOR_LOGIN = '{"code":400,"message":"Недостаточно данных для входа"}'
    ACCOUNT_NOT_FOUND = '{"code":404,"message":"Учетная запись не найдена"}'



class DataOrder:

    order_data = {
        "firstName": "Thomas",
        "lastName": "Shelby",
        "address": "1510 Sweet Apple Ct Birmingham, Alabama(AL), 35242",
        "metroStation": 4,
        "phone": "+7 999 000 11 22",
        "rentTime": 5,
        "deliveryDate": "2024-12-30",
        "comment": "В пабах люди много чего болтают. Чаще всего, за них говорит виски.",
        "color": []
    }

    scooter_color = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]
    







