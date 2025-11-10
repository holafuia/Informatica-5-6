import requests
import json

def main():
    universities = {
        "bYU_PATHWAY": {
            "majors": 30,
            "semester_cost": 3000,
            "closest_campus": "online, 0 km"
        },
        "EAC": {
            "majors": 140,
            "semester_cost": 0,
            "closest_campus": "thatcher, 466 km"
        },
        "AUCJ": {
            "majors": 37,
            "semester_cost": 5000,
            "closest_campus": "ciudad juarez, 280 km"
        },
        "TEC_MILENIO": {
            "majors": 24,
            "semester_cost": 25000,
            "closest_campus": "ciudad juarez, 280 km"
        },
        "TEC_DE_MONTERREY": {
            "majors": 44,
            "semester_cost": 160000,
            "closest_campus": "monterrey, 920"
        }
    }
    uni(universities)

def uni(universities):
    for y in universities:
        y.replace("_", " ")
    while True:
        try:
            x = input("please type in the university you are looking for: ").capitalize()
            if x in universities:
                print(universities[x])
        except ValueError:
            print("invalid university")
            continue

main()