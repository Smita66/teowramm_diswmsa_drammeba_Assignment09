
import requests
import json 

class Cat():
    response = requests.get('https://cataas.com/api/cats?tags=cute')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    print(parsed_json)
    
    
    
    

    
    
    
