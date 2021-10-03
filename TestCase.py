import pytest
import requests

def test_page():
   url = "http://127.0.0.1:5000/v1/sanitized/input" 
   req = requests.post(url)
   assert req.status_code == 200 