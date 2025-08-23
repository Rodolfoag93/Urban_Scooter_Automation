import requests
import data


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

    #def create_order(self, order_data):
        #print("\nCreando una nueva orden...")
        #endpoint = "/api/v1/orders"
        #url = self.base_url + endpoint
        #try:
            #response = requests.post(url, json=order_data, headers=self.headers)
            #print(f"Estado de la respuesta: {response.status_code}")
            #print(f"Cuerpo de la respuesta: {response.json()}")

            # Verificar si la orden se creó exitosamente
            #if response.status_code == 201:
             #   return response.json().get("track")
#            return None
 #       except requests.exceptions.RequestException as e:
  #          print(f"Error al conectar con la API para crear la orden: {e}")
   #         return None



if __name__ == "__main__":

    courier_api = CourierApi(data.API_Url_Urban_Routes)

    # Datos para crear una orden de ejemplo
    example_order_data = {
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St",
        "metroStation": 4,
        "phone": "+1 555-1234",
        "rentTime": 5,
        "deliveryDate": "2024-12-31",
        "comment": "Tocar el timbre dos veces",
        "color": ["BLACK"]
    }


#    track_number = courier_api.create_order(example_order_data)

#    if track_number is not None:
#        print(f"\n¡Orden creada exitosamente! Track number: {track_number}")
#    else:
#        print("\nFallo al crear la orden. Terminando el script.")
