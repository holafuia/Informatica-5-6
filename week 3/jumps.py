def ber(so):
    return so.isnumeric()

number = input("Write the number limit: ")
while not ber(number):
    number = input("Write the number limit: ")

num = input("Write the desired step size: ")
while not ber(num):
    input("Write the desired step size: ")

num = int(num)
number = int(number)
x = num

if num > 0:
    while num <= number:
        print(num)
        num = num + x
else:
    print("NO")

print("execution has ended")