#syntax error
#print("hello, world)

#value error
# try:
#     x = int(input("what's x? "))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number")

#zero division error
# def spam(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print("error")

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# while True:
#     try:
#         x = int(input("what's x? "))
#     except ValueError:
#         print("x is not a number")
#     else:
#         print(f"x is equal t0 {x}")
#         break

def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            number = int(input_str)
            if number < 100 and number >= 0:
                return number
        except ValueError:
            pass
        
number = read_small_integer()
print(number, "to the power of 3 is: ", number**3)