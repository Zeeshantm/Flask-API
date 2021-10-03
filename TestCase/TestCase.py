import pytest
import requests
import json
import logging

logging.basicConfig(filename="logfile.log",filemode='w')

url = "http://127.0.0.1:5000" 

def test_case1():
   req = requests.get(url+'/v1/sanitized/input')
   assert req.status_code == 200
   data = req.json()
   assert data['status'] == 'Get Method Working'

def test_case2():
   url = "http://127.0.0.1:5000/v1/sanitized/input"

   #Body
   payload = {"payload": "hakdga"}
   
   #Adding Header
   headers = {'Content-Type': 'application/json'}
   
   #Convert dict to json string by json.dumps() for body data
   response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
   
   #Validate response header and body contents
   assert response.status_code == 200
   resp_data = response.json()
   assert resp_data['Result'] == 'Sanitized'
   
   #log response body as text
   logging.info(response.text)