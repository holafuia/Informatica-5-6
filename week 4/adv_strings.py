#string length
input_string = input("Please type a message: ")
# print(input_string)

# print("-" * len(input_string))

# #string index
# print(input_string[0:2])
# print(input_string[1])
# print(input_string[-1])

#example
# i = -1
# while i < len(input_string):
#     print(input_string[i])
#     i -= 1
#     if i*-1 > len(input_string):
#         break

print("h" in input_string)
print("j" in input_string)
print("ello" in input_string)
print(input_string.find("l"))