capitals = {
    "Mexico": "Mexico City",
    "Canada": "Ottawa",
    "Brazil": "Brasilia",
    #"Canada": "Montreal" #It will replace the other one
} #this is a dictionary, both words are in the same space

capitals["Italy"] = "Rome"
# print(capitals["Canada"]) #prints the thing after the :
del capitals["Brazil"]
capitals.pop("Canada")
capitals.clear()
#print(capitals) # prints the whole dictionary

# houses = {
#     "Harry Potter": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# print(houses)

# for house in houses:
#     h = houses[house]
#     print(f"{house}: {h}") # the first one prints the first part and the h the second

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for element in students:
    print(f"{element["name"]}, {element["house"]}, {element["patronus"]}")