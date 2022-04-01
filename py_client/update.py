import requests

endpoint = "http://localhost:8000/api/products/1/update"

data = {"title": "this is the updated title", "price": 76.34}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
