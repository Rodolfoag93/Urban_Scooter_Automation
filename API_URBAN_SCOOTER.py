import requests
import data

base_url = data.API_Url_Urban_Routes


class CourierApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def create_courier(self, login, password, first_name):
        print(f"Creando un nuevo courier: {login}")
        endpoint = "/api/v1/courier"
        url = self.base_url + endpoint
        courier_data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        try:
            response = requests.post(url, json=courier_data, headers=self.headers)
            print(f"Estado de la respuesta: {response.status_code}")
            print(f"Cuerpo de la respuesta: {response.json()}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API para crear un courier: {e}")
            return None

    def login_courier(self, login, password):
        print(f"\nIniciando sesión con el courier: {login}")
        endpoint = "/api/v1/courier/login"
        url = self.base_url + endpoint
        login_data = {
            "login": login,
            "password": password
        }
        try:
            response = requests.post(url, json=login_data, headers=self.headers)
            print(f"Estado de la respuesta: {response.status_code}")
            print(f"Cuerpo de la respuesta: {response.json()}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API para iniciar sesión: {e}")
            return None

