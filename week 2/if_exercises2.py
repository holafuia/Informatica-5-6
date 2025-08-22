def main():
    x = int(input("write the first number: "))
    y = input("write the desired operation by symbol(*,-,+): ")
    z = int(input("write the second number: "))
    so(x, y, z)

def so(x, y, z):
    if y == "*":
        print(x * z)
    if y == "-":
        print(x-z)
    if y == "+":
        print(x+z)

main()