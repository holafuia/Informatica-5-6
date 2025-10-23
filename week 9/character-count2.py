message = input("write a message: ")
dictionary = {}

def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1

    print(dictionary)

character_counter(message, dictionary)