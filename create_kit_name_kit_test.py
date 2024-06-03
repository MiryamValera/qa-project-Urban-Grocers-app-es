import sender_stand_request
import data

#FUNCIÓN QUE CAMBIA EL VALOR EN EL PARÁMETRO 'NAME'
def get_user_kit(user_kit):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = user_kit
    return current_kit_body

#FUNCIÓN - PRUEBA POSITIVA
def positive_assert(user_kit):
    user_kit_body = get_user_kit(user_kit)
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)

    assert response_new_kit.status_code == 201
    assert response_new_kit.json()["name"] == user_kit_body["name"]

#FUNCIÓN - PRUEBA NEGATIVA
def negative_assert_symbol(user_kit):
    user_kit_body = get_user_kit(user_kit)
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(user_kit_body)

    assert response_new_kit.status_code == 400

#FUNCIÓN - PRUEBA NEGATIVA - TEST 8 SIN PASAR EL PARÁMETRO 'NAME'
def negative_assert_no_name(kit_body):
    sender_stand_request.post_new_user(data.user_body)
    response_new_kit = sender_stand_request.post_new_kit(kit_body)

    assert response_new_kit == 400


#PRUEBA 1. EL NÚMERO PERMITIDO DE CARACTERES (1)
def test_create_user_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_test_1)

#PRUEBA 2. EL NÚMERO PERMITIDO DE CARACTERES (511)
def test_create_user_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_test_2)

#PRUEBA 3. EL NÚMERO DE CARACTERES ES MENOR QUE LA CANTIDAD PERMITIDA (0)
def test_create_user_kit_empty_name_get_error_response():
    negative_assert_symbol(data.kit_test_3)

#PRUEBA 4. EL NÚMERO DE CARACTERES ES MAYOR QUE LA CANTIDAD PERMITIDA (512)
def test_create_user_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_test_4)

#PRUEBA 5. SE PERMITEN CARACTERES ESPECIALES EN EL PARÁMETRO 'NAME'
def test_create_user_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_test_5)

#PRUEBA 6. SE PERMITEN ESPACIOS EN EL PARÁMETRO 'NAME'
def test_create_user_kit_has_space_in_name_get_success_response():
    positive_assert(data.kit_test_6)

#PRUEBA 7. SE PERMITEN NÚMEROS EN EL PARÁMETRO 'NAME'
def test_create_user_kit_has_numbers_in_name_get_success_response():
    positive_assert(data.kit_test_7)

#PRUEBA 8. EL PARAMETRO 'NAME' NO SE PASA EN LA SOLICITUD
def test_create_user_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

#PRUEBA 9. SE HA PASADO UN TIPO DE PARÁMETRO DIFERENTE (NÚMERO)
def test_create_user_kit_has_data_type_number_in_name_get_error_response():
    negative_assert_symbol(data.kit_test_9)