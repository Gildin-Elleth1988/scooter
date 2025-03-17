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
