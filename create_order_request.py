import configuration
import data
import requests

#создаем новый заказ
def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

#получаем заказ по треку
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))