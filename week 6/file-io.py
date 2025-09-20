# names = []

# for i in range(3): #la mugre repite 3 veces
#     names.append(input("What's your name? "))

# for name in sorted(names): # sortea los de arriba
#     print(f"Hello {name}")

# name = (input("What's your name? ")) # agrega texto
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "a") as file: # lo mismo que el de arriba
#     file.write(f"{input("What's your name? ")}")

with open("names.txt", "r") as file: # it let's you see the text file
    lines = file.readlines()
for line in sorted(lines):
    print(line.strip())