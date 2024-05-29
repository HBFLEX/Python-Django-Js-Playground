import requests


endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, data={"description": "nyama", "price": 34.75})


print(response.json())
print(response.status_code)