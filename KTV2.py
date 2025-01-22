# brandid = input("Mida otsid?: ")
import requests

url = "https://dummyjson.com/products"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for brandid in "products":
        brandid = data["products"]
        print(brandid)
else:
    print("Viga")



