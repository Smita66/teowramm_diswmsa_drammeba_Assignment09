
import requests
import json

class Car:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model_urls = { # creating our dictionary
            'camry': 'https://api.api-ninjas.com/v1/cars?model=camry',
            'corolla': 'https://api.api-ninjas.com/v1/cars?model=corolla',
            'bmw': 'https://api.api-ninjas.com/v1/cars?model=bmw',
            'chevrolet': 'https://api.api-ninjas.com/v1/cars?model=chevrolet'
        }
        self.car_models = list(self.model_urls.keys()) #getting dictionary keys

        
        