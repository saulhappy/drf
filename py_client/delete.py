from urllib import response
import requests

p_id = input("Enter product id: \n")

p_id = int(p_id)

endpoint = f"http://localhost:8000/api/products/{p_id}/delete/"
get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code==204)
