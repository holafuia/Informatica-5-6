import json
import requests

def main():
    num_trade = float(input("How many bitcoins do you want to trade? "))
    key = "0c826c2fab20a545e5470a6e85ccd02a39773a23d1d1edfc84e90402d74ba6d9"
    bitcoin = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={key}").json()
    print(bitcoin)

main()