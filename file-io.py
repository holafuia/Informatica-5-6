# names = []

# for i in range(3): #la mugre repite 3 veces
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"Hello {name}")

name = (input("What's your name? "))
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()