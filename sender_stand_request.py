import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track),
                         headers=data.headers)

# Шаг 1: Создание заказа
response = post_new_order(data.order_body)
assert response.status_code == 201, f"Ошибка: {response.status_code}"
track = response.json().get("track")
print("Трек заказа:", track)

# Шаг 2: Получение заказа по треку
response = get_order(track)
assert response.status_code == 200, f"Ошибка: {response.status_code}"
print("Данные заказа:", response.json())