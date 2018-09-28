import requests
from pyquery import PyQuery as pq
import json



url = "http://45.40.204.149:8000/circuit-new"

data = {}

response = requests.get(url)
print(response.json())
recv = response.json()
print(recv['current_page'])
print(recv.get('current_page'))
print(response.status_code)