def main():
    n1 = int(input("number 1: "))
    n2 = int(input("number 2: "))
    n3 = int(input("number 3: "))
    n4 = int(input("number 4: "))

    if n1 > n2 and n1 > n3 and n1 > n4:
        greatest = n1
    elif n2 > n3 and n2 > n4:
        greatest = n2
    elif n3 > n4:
        greatest = n3
    else:
        greatest = n4

    print(f"{greatest}")

main()