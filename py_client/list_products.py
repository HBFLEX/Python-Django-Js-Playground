import requests
from getpass import getpass


endpoint = "http://localhost:8000/api/auth/"
username = str(input("Username: "))
password = getpass()
user_data = { "username": username, "password":  password }

# send data
auth_response = requests.post(endpoint, json=user_data)
token = auth_response.json().get('token')

if token:

    # set the authorization headers
    headers = { "Authorization": f"Bearer {token}" }
    # send a request
    endpoint = "http://localhost:8000/products"
    response = requests.get(endpoint, headers=headers)

    print(response.json())
else:
    print("The token was not provided or valid!")