import pytest
import allure
import requests
from data import TestData, ResponseTexts
from conftest import create_courier
from conftest import create_two_identic_couriers_login
from conftest import create_two_identic_couriers_data


@allure.suite('Тестирование ручки создания курьера')
class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера, когда все обязательные поля заполнены')
    def test_new_courier_registration_all_inputs_are_fill(self, create_courier):
        courier_data = create_courier

        response = requests.post(f'{TestData.NEW_COURIER_URL}', json=courier_data)
        assert response.status_code == 201 and response.text == ResponseTexts.SUCCESSFUL_CREATION
        print(response.status_code)
        print(response.text)

    @allure.title('Проверка, что нельзя создать двух курьеров с одинаковыми логинами')
    def test_can_not_create_identic_couriers_login(self, create_two_identic_couriers_login):

        requests.post(f'{TestData.NEW_COURIER_URL}', data=create_two_identic_couriers_login[0])
        response = requests.post(f'{TestData.NEW_COURIER_URL}', data=create_two_identic_couriers_login[1])
        assert response.status_code == 409 and response.text == ResponseTexts.LOGIN_ALREADY_USED_ERROR
        print(response.status_code)
        print(response.text)

    @allure.title('Проверка, что нельзя создать двух курьеров с одинаковыми данными')
    def test_can_not_create_identic_couriers_data(self, create_two_identic_couriers_data):

        requests.post(f'{TestData.NEW_COURIER_URL}', data=create_two_identic_couriers_data[0])
        response = requests.post(f'{TestData.NEW_COURIER_URL}', data=create_two_identic_couriers_data[1])
        assert response.status_code == 409 and response.text == ResponseTexts.LOGIN_ALREADY_USED_ERROR
        print(response.status_code)
        print(response.text)

    @allure.title('Проверка, что если одно из обязательных полей не заполнено, то возвращается ошибка ')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_create_courier_with_incomplete_input(self, create_courier, key, value):
        create_courier[key] = value
        response = requests.post(f'{TestData.NEW_COURIER_URL}', data=create_courier)
        assert response.status_code == 400 and response.text == ResponseTexts.NOT_ENOUGH_DATA_ERROR
        print(response.status_code)
        print(response.text)


