def main ():
    price = 50
    total_paid = 0
    vending_machine(price, total_paid)

def vending_machine(price, total_paid):
    name = input("Name plis: ")
    while price > 0:
        print(f"amount due: {price}")
        pay = int(input("insert coin: "))

        if pay == 25 or pay == 10 or pay == 5:
            price == price - pay
            total_paid = total_paid + pay
        else:
            print("not a coin.")

    if total_paid >= 50:
        print(f"thanks! Here's a coke for {name}")
        print(f"Your change is {total_paid - 50}")

main()