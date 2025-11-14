import json
import requests

def main():
    while True:
        try:
            num_trade = float(input("How many bitcoins do you want to trade? "))
            key = "0c826c2fab20a545e5470a6e85ccd02a39773a23d1d1edfc84e90402d74ba6d9"
            bitcoin = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={key}").json()
            print(f"bitcoin value right now: {bitcoin["data"].get("priceUsd")}")
            bitcoin_count = num_trade * float(bitcoin["data"].get("priceUsd"))
            print(f"Your total value would be: ${round(bitcoin_count, 2)}")
            break
        except:
            print("error")

main()