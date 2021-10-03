import pytest
import requests
from API import home
import json

url = "http://127.0.0.1:5000" 

def test_case():
   req = requests.get(url+'/v1/sanitized/input')
   assert req.status_code == 200
   data = req.json()
   assert data['status'] == 'Get Method Working'

def test_case1():
   url = "http://127.0.0.1:5000/v1/sanitized/input"
   payload = {"payload": "hakdga"}
   headers = {'Content-Type': 'application/json'}
   response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
   assert response.status_code == 200
   resp_data = response.json()

   assert resp_data['Result'] == 'Sanitized'

   print(response.text)
   

