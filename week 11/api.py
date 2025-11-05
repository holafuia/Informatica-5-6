import requests
import json

song = input("What song are you looking for: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term="+song)
# print(json.dumps(response.json(), indent=2))

search = response.json()
for result in search["results"]:
    print(f"{result["trackName"]} by {result["artistName"]}")

city = input("city: ")
response2 = requests.get("http://goweather.xyz/weather/"+city)
print(response2.json())