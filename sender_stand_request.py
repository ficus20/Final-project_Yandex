import configuration
import requests
import data

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                     json=body,
                     headers=data.headers)

def get_order(number_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                       params={"t": number_track})




