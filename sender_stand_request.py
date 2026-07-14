import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#crear un kit usando el authoToken del usuario
def post_new_client_kit(kit_body,auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
#clave authorizacion, bearer lo exige la api para el token de autorización
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
#XXse toma el nombre del kit y el token del usuario, se agrega al token al encabezado authorization y envia solicitud para crear kit a ese usuario






