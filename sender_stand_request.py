import configuration
import requests
import data

#CREAR UN USUARIO NUEVO
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json()['authToken'])


#CREAR UN KIT NUEVO DEL USUARIO
def post_new_kit(kit):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + response.json()["authToken"]
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json= kit,
                         headers= current_headers)

response_kit = post_new_kit(data.kit_body)
print((response_kit.status_code))
print(response_kit.text)

