#!/usr/bin/python
import requests

response = requests.get('http://joedye.me/pi-order/config')

print(response.json())

