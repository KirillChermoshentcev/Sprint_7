import pytest
import allure
import requests
import helpers
from data import TestData, ResponseTexts
from conftest import create_courier, login_courier


@allure.suite('Тестирование ручки для логина курьера')
class TestLoginCourier:

    @allure.title('Проверка, что авторизация прошла успешно, у курьера есть свой ID')
    def test_login_successful(self, login_courier):
        requests.post(f'{TestData.NEW_COURIER_URL}', json=login_courier)
        response = requests.post(f'{TestData.LOGIN_COURIER_URL}', json=login_courier)
        assert response.status_code == 200 and response.json()["id"] is not None
        print(response.json()["id"])

    @allure.title('Проверка, что авторизация не произойдет, если не передать обязательные параметры логина или пароля')
    @pytest.mark.parametrize('key, value', [('login', ''),('password', '')])
    def test_auth_not_happen_without_login_or_password(self, create_courier, key, value):
        create_courier[key] = value
        response = requests.post(f'{TestData.LOGIN_COURIER_URL}', json=create_courier)
        assert response.status_code == 400 and response.text == ResponseTexts.NOT_ENOUGH_DATA_FOR_LOGIN
        print(response.text)

    @allure.title('Проверка, что авторизация не происходит, если указать несуществующий логин(неверный)')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateCourierData.generate_new_courier_data()),
                                            ('password', helpers.GenerateCourierData.generate_new_courier_data())])
    def test_account_not_found(self, create_courier, key, value):
        requests.post(f'{TestData.NEW_COURIER_URL}', json=create_courier)
        create_courier[key] = value
        response = requests.post(f'{TestData.LOGIN_COURIER_URL}', data=create_courier)
        assert response.status_code == 404 and response.text == ResponseTexts.ACCOUNT_NOT_FOUND