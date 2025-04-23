import requests
from getpass import getpass

username = input('your username?\n')
password = getpass('type your passcode:\n')

auth_endpoint = "http://localhost:8000/api/auth/"

auth_response = requests.post(auth_endpoint, json={'username' : username, 'password' : password}) 
print(auth_response.json())




if auth_response.status_code == 200:
    token = auth_response.json()['token']
    # headers = {
    #     'Authorization': f'Token {token}'
    # }
    headers = {  # for 'Bearer', need to override TokenAuthentication class & keyword='Bearer'
        "Authorization": f"Bearer {token}" 
    }

    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers) 
    print(get_response.json())
    # print(get_response.status_code)
