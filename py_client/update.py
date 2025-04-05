import requests

endpoint = "http://localhost:8000/api/products/3/update/"

data = {
    "title": "title - edited",
    "price": 75.99
}
get_response = requests.put(endpoint, json=data) 
print(get_response.json())
# print(get_response.status_code)
