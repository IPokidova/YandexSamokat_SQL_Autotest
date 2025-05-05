#Ирина Покидова, 29А когорта. Финальный поект. Инженер по тестированию плюс
import configuration
import data
import requests
import create_order_request
  
#функция для получения заказа по треку 
def test_get_order_by_track():
    #получаем трек заказа
    track=create_order_request.post_create_order(data.order_body).json()['track']
    # получаем данные заказа по треку
    response=create_order_request.get_order_by_track(track)
    assert response.status_code == 200
   