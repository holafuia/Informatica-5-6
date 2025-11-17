import requests
import json

def main():
    api_key = "12MTRNXM5HQ6"
    while True:
        try:
            timezone = input("Type 1 to see the timezones list, type 2 to type the desired timezone: ")
            if timezone == "2":
                info = input("Type the timezone you want to see the hour: ")
                api = requests.get(f"http://api.timezonedb.com/v2.1/get-time-zone?key={api_key}&format=json&by=zone&zone={info}").json()
                if info == api["zoneName"]:
                    print(f"the time is: {api["formatted"][11:19]}")
                    break
                else:
                    print("Invalid timezone")
            elif timezone == "1":
                print("Asia, America, Africa, Pacific, Europe, Antarctica, Australia, Atlantic, Indian, Arctic")
                continent = input("type the desired continent: ")
                api2 = requests.get(f"http://api.timezonedb.com/v2.1/list-time-zone?key={api_key}&format=json&zoneName=*{continent}*").json()
                for all_zones in api2["zones"]:
                    zone = all_zones["zoneName"][:len(continent)]
                    if zone == continent:
                        print(all_zones["zoneName"])
            else:
                print("Invalid")
        except:
            print("An Unexpected Error Happened")

main()