import pytest
import requests
import json
import allure
from data import DataOrder, TestData


@allure.suite('Тестирование возможности выбора цвета при заказе')
class TestCreateOrder:

    @allure.title('Проверка, что во время создания заказа, можно указать один цвет, два цвета или совсем не указывать ')
    @pytest.mark.parametrize('color', DataOrder.scooter_color)
    def test_possibility_of_choosing_scooter_color(self, color):
        customer_data = DataOrder.order_data
        customer_data['color'] = color
        customer_data_json = json.dumps(customer_data)
        response = requests.post(f'{TestData.CREATE_ORDER_URL}', json=json.loads(customer_data_json))
        resp_json = response.json()
        assert response.status_code == 201 and 'track' in resp_json

