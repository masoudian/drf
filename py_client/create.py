import requests

endpoint = "http://localhost:8000/api/products/"

headers = {'Authorization': 'Bearer 58c381c00cb64f30a728ce9f7967025d4d5c72cd'}

data = {
    "title": "this is titleeeee",
    "price": 77.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())
# print(get_response.status_code)
