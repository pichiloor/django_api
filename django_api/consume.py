from urllib import response
import requests

response = requests.get('http://127.0.0.1:8000/rooms/')
print(response.json())

response = requests.get('http://127.0.0.1:8000/events/')
print(response.json())

response = requests.get('http://127.0.0.1:8000/booking/')
print(response.json())
