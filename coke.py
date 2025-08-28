def number(so):
    return so.isnumeric()

name = input("insert your name: ")
print("coke is 50 cents, acceptable cents: 25, 10, 5")
y = 0
while True:
    cents = input("insert the cents: ")
    while not number(cents):
        cents = input("insert the cents: ")
    
    if int(cents) == 25 or int(cents) == 10 or int(cents) == 5:
        y = int(y) + int(cents)
        print(f"balance: {y}")

        if y > 50:
            break
    else:
        print("pay error")

x = int(y) - 50
print(f"here's a coke for {name}")
print(f"your change is {x} cents")