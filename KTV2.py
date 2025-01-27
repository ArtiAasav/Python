# brandid = input("Mida otsid?: ")
import requests

url = "https://dummy-json.mock.beeceptor.com/posts"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    otsing = input("Millist tiitlit otisd: ")
    for title in data:
        tiitel = title["title"]
        if otsing in tiitel:
            print(f"Pealkiri: {tiitel}")
else:
    print("Viga")



