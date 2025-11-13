import requests
import json
#&window_width=1920&window_height=1080&timeout=45000
#url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffunctions.html

def main():
    info = input("Type the python function you wnat to know: ")
    api_key = "sb_e9a4fe336b9bc7c02b78ffb59101e6c7e7e8c42bd70de987e30b6feb85babb36"
    api = requests.get(f"https://scrapingbot.io/api/v1/scrape?api_key={api_key}&url=https://docs.python.org/3/library/functions.html&render_js=true&block_resources=true").json()
    print(api)

main()