import pytest
import requests
from data import TestData
from helpers import GenerateCourierData


@pytest.fixture
def create_courier():
    courier_data = GenerateCourierData.generate_new_courier_data()
    yield courier_data
    login_response = requests.post(f'{TestData.LOGIN_COURIER_URL}', json=courier_data)
    if login_response.status_code == 200:
        courier_id = login_response.json().get('id')
        requests.delete(f'{TestData.DELETE_COURIER}{courier_id}')


@pytest.fixture
def create_two_identic_couriers_login():
    courier_1 = GenerateCourierData()
    courier_2 = GenerateCourierData()
    return courier_1.create_courier_with_identic_login(), courier_2.create_courier_with_identic_login()

@pytest.fixture
def create_two_identic_couriers_data():
    courier_1 = GenerateCourierData()
    courier_2 = GenerateCourierData()
    return courier_1.create_courier_with_identic_data(), courier_2.create_courier_with_identic_data()


@pytest.fixture
def login_courier(create_courier):
    create_courier['firstName'] = ''
    return create_courier