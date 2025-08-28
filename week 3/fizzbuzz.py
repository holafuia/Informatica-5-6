def main():
    number = int(input("write a WHOLE number: "))
    y = number/2

    if number % 3 == 0 and number % 5 == 0:
        x = "FIZZBUZZ"
    elif number % 5 == 0:
        x = "BUZZ"
    elif number % 3 == 0:
        x = "FIZZ"
    else:
        x = number

    if y == 0 or number/2 == 0:
        print("Prime", x)
    else:
        print(x)

main()