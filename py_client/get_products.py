import requests

endpoint = "http://localhost:8000/api/products"
token_endpoint = 'http://localhost:8000/api/token/'


# get token
user_data = { "username": 'hbfl3x', 'password': 'soundplay265' }
response = requests.post(token_endpoint, json=user_data)

if response:
    response = requests.get(endpoint, headers={'Authorization': f'Bearer {response.json().get('access')}'})

print(response.json())
