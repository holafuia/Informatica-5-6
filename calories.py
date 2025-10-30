def main():
    calories()

def calories():
    dictionary = {
        "milk": "73",
        "skim": "45",
        "plain low-fat": "77",
        "sour cream light": "16",
        "egg": "75",
        "egg white": "16",
        "cream cheese": "51",
        "american pasteurized": "79",
        "lentils boiled": "115",
        "pinto beans boiled": "122",
        "catfish baked": "89",
        "chicken deli": "20",
        "peanuts roasted": "166",
        "almonds dry roasted": "170",
        "corn": "59",
        "celery": "1",
        "watermelon": "11",
        "pears": "20",
        "ranch": "73",
        "quinoa cooked": "56"
    }
    while True:
        while True:
            pick = input("please type the food type to see its calories: ").lower().strip()
            if pick not in dictionary:
                print("Not Valid")
                continue
            break
        while True:
            otherpick = input("please type the second food type to see its calories: ").lower().strip()
            if otherpick not in dictionary or otherpick == pick:
                print("Not Valid")
                continue
            break
        

main()
