import requests

hey = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")

data = hey.json()

with open("output.txt", 'a', encoding='utf-8') as file:
        file.write(data["extract"])
