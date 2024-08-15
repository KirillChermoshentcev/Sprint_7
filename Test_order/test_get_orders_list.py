import requests
import allure
from data import TestData


@allure.suite('Тестирование списка заказов')
class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_orders_list(self):
        response = requests.get(f'{TestData.GET_ORDER_LIST}')
        assert response.status_code == 200 and 'orders' in response.json()