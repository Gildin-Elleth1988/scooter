import requests
import configuration
import data
from sender_stand_request import post_new_order, get_order


def test_order():
    response = post_new_order(data.order_body)
    # проверка, что создалось, получаем трек
    assert response.status_code == 201, f"Ошибка: {response.status_code}"
    track = response.json().get("track")
    # print("Трек заказа:", track)
    # проверка получения заказа по треку
    response = get_order(track)
    assert response.status_code == 200, f"Ошибка: {response.status_code}"
    # print("Данные заказа:", response.json())
