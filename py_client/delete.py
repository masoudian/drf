import requests

# endpoint = "http://localhost:8000/api/products/3/delete/"


prod_id = input('insert id to delete: > ')
try:
    prod_id = int(prod_id)
except:
    prod_id =None
    print('not valid')

if prod_id:
    endpoint = f"http://localhost:8000/api/products/{prod_id}/delete/"

get_response = requests.delete(endpoint) 
# print(get_response.json())
print(get_response.status_code, get_response.status_code==204)
