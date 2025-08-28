while True:
    response = input("someone arrives, say something: ").title()

    if response.startswith("Hello"):
        print("balance: 0$")
    elif response.startswith("H"):
        print("balance: 20$")
    else:
        print("balance: 100$")
        break
print("¡Thanks For Coming, Come Back Soon!")