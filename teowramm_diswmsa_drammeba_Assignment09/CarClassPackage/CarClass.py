
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
        
    def get_car_info(self, model):
        api_url = f'https://api.api-ninjas.com/v1/cars?model=model'
        response = requests.get(api_url, headers={'X-Api-Key': self.api_key})
        if response.status_code == requests.codes.ok:
            return json.loads(response.content)
        #https://www.geeksforgeeks.org/json-loads-in-python/
        # https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/?ref=ml_lbp
        #https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/?ref=ml_lbp
        else:
            return None
        
        