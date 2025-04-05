import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this is titleeeee",
    "price": 77.99
}
get_response = requests.get(endpoint) 
print(get_response.json())
# print(get_response.status_code)
