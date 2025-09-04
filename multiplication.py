def positive(so):
    return so.isnumeric()

number = input("please write a positive number from 1 to 10: ")
while not positive(number) or int(number) < 1 or int(number) > 10:
    number = input("please write a positive number from 1 to 10: ")

i = 1
while i <= int(number):
    s = 1
    while s <= int(number):
        print(f"{i} x {s} =", i*s)
        s += 1
    i += 1
    print("")