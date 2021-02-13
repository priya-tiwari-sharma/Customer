import json
import requests
from django.core.files import File

URL='http://127.0.0.1:8000/customerapi/'
def get_data(username=None):
    data={}
    if username is not None:
       data={'username':username}                    #python dict.
    json_data=json.dumps(data)            #converting python dict. to  json data
    r=requests.get(url=URL,data=json_data)  # fetch show/ url and get request
    data=r.json()                         # extract all json data 
    print("username======",username)
    print(data)

# get_data('priya@')

def post_data(username=None):
    
    data={
    "name":"viaan",
    "age":10,
    "dob":"2021-12-08",
    "email":"viaan.ab21@gmail.com",
    "state":"delhi",
    "username":"viaan@",
    "password":123,
  
    }
    json_data=json.dumps(data)            #converting python dict. to  json data
    r=requests.post(url=URL,data=json_data)  # fetch show/ url and get request
    data=r.json()                         # extract all json data 
 
    print(data)

get_data('viaan@')