import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'abc': 123}, json={'query': 'hello world'}) # http request

print(get_response.json())
print(get_response.status_code)
