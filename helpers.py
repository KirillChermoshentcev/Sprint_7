from faker import Faker

faker = Faker()


class GenerateCourierData:

    @staticmethod
    def generate_new_courier_data():

        email = faker.email()
        password = faker.password()
        first_name = faker.first_name()

        payload = {
            "login": email,
            "password": password,
            "firstName": first_name
        }
        return payload

    def create_courier_with_identic_login(self):

        email = 'SoloveiRazboynik'
        password = faker.password()
        first_name = faker.first_name()

        payload = {
            "login": email,
            "password": password,
            "firstName": first_name
        }
        return payload

    def create_courier_with_identic_data(self):

        email = 'qwerty@qwert.com'
        password = '1234567'
        first_name = 'Qwertylos'

        payload = {
            "login": email,
            "password": password,
            "firstName": first_name
        }
        return payload

    def create_courier_with_empty_fill(self):

        email = ''
        password = faker.password()
        first_name = faker.first_name()

        payload = {
            "login": email,
            "password": password,
            "firstName": first_name
        }
        return payload
