# brandid = input("Mida otsid?: ")
import requests

url = "https://dummy-json.mock.beeceptor.com/posts"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for title in "products":
        title = data["products"]["title"]
        print(title)
else:
    print("Viga")



