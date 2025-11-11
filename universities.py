import requests
import json

def main():
    universities = {
        "BYU_PATHWAY": {
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
    while True:
        try:
            university = input("please type in the university you are looking for: ").upper()
            university = university.replace(" ", "_")
            for individual in universities:
                if university == individual:
                    for single_unit in universities[university]:
                        print(f"{single_unit}: {universities[university].get(single_unit)}")
                    break
            other_choises = requests.get("https://raw.githubusercontent.com/Hipo/university-domains-list/refs/heads/master/world_universities_and_domains.json&term="+university)
            for one in other_choises:
                if one.get("name") == university:
                    print(f"{one["web_pages"]} \n {one["country"]} \n {one["state-province"]}")
                    break
        except ValueError:
            print("invalid university")

main()