import time

def main():
    characters = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser"]

    for loop in characters:
        if loop == "Princess Peach":
            continue
        invitation(loop)
        time.sleep(0.5)

def invitation(x):
    print("~" * 76)
    print(f"Dear {x}")
    print("")
    print("You are cordially invited to a ball at Peach's Castle this evening, 7:00 PM.")
    print("")
    print("sincerely,")
    print("Princess Peach")
    print("~" * 76)
    print("")

main()