import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#crear un nuevo usuario
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]

def positive_assert(name):
 #copia de kit body con el valor de name a probar
    kit_body = get_kit_body(name)
     #obtiene el valor del authoToken que se necesita para crear el kit del usuario, para decirle a la API a que usuario pertenece el kit
    auth_token = get_new_user_token()
     # Guardar la respuesta de la solicitud para crear un kit utilizando el authToken del usuario del archivo sender.
    kit_response = sender_stand_request.post_new_client_kit( kit_body, auth_token )

    assert kit_response.status_code == 201
    #verificar que el nombre que devuelve la api es igual al nombre enviado
    assert kit_response.json()["name"] == kit_body["name"]
#verificar el kit con nombre a se creó correctamente


def negative_assert(name):
    kit_body=get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit( kit_body, auth_token )

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

def negative_assert_empty_name(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit( kit_body,auth_token)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

#prueba 1 	El número permitido de caracteres (1)
def test_create_kit_1_letter_get_success_response():
    positive_assert("a")

#prueba 2 	El número permitido de caracteres (511)
def test_create_kit_511_letter_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#prueba 3 El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_zero_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = ""
    negative_assert("")

#prueba 4 El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#prueba 5 Se permiten caracteres especiales
def test_create_kit_special_letters_get_sucess_response():
    positive_assert('"N%@","')

#prueba 6 Se permiten espacios
def test_create_kit_empty_space_get_sucess_response():
    positive_assert(" A Aaa ")

#prueba 7 se permiten números
def test_create_kit_numbers_string_get_sucess_response():
    positive_assert("123")

#prueba 8 El parámetro no se pasa en la solicitud
def test_create_empty_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_empty_name(kit_body)

#prueba 9	Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_number_type_get_error_response():
    negative_assert(123)



