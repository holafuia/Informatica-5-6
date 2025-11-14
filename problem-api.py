import requests
import json
#&window_width=1920&window_height=1080&timeout=45000
#url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffunctions.html

def main():
    info = input("Type the continent you want to see the hour: ")
    info2 = input("Type the state you want to see the hour: ")
    api_key = "yBkWF/PU1+iJLkRRJ8BJGw==0es4ug9tt26N273e"
    api = requests.get(f"https://api.api-ninjas.com/v1/timezone?timezone={info}", headers={"X-Api-Key": api_key}).json()
    print(api)

main()