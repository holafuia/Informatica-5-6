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
    if pick == "milk" or pick == "watermelon" and otherpick == "milk" or otherpick == "watermelon":
        print("Not a good conbination, you are going to explode")
    else:
        print(f"{pick} has {dictionary[pick]} calories and {otherpick} has {dictionary[otherpick]} calories. Total calories {int(dictionary[pick]) + int(dictionary[otherpick])}")

main()
