import requests
import data

#crear un nuevo courier
endpoint_new_courier = "/api/v1/courier"
URL_new_courier = data.Urban_routes_URl + endpoint_new_courier
courier = {
    "login": "juan",
    "password": "1234",
    "firstName": "juanito"
}

req = requests.post(URL_new_courier, json=courier)
print(req.status_code)
print(req.json())

#hacer login de usuario del courier
endpoint_courier_login = "/api/v1/courier/login"
URL_courier_login = data.Urban_routes_URl + endpoint_courier_login
login = {
    "login": "juanito",
    "password": "1234"
}
req = requests.post(URL_courier_login, json=login)
print(req.status_code)
print(req.json())

