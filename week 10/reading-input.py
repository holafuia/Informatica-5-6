def main():
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

def read_input(x, y, z):
    while True:
        try:
            number = int(input(x))
            if int(y) <= number <= int(z):
                return number
            else:
                print("Between 5 and 10")
        except ValueError:
            print("A NUMBER")
            pass

main()