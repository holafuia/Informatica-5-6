def main():
    factorial()

def factorial():
    while True:
        try:
            number = int(input("Please type a positive factorial number: "))
            if number != 0:
                result = number
                sub = number - 1
                for num in range(number - 1):
                    result = result * sub
                    sub = sub - 1
            if number == 1 or number == 0:
                print(f"the factorial number of {number} is 1")
                break
            elif number < 0:
                raise ValueError
            elif number > 0:
                print(f"the factorial number of {number} is {result}")
                break
        except:
            print("error")

main()