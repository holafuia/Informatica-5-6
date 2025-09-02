def main():
    message = input("write a message: ").lower()
    encode_message(message)

def encode_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    new_message = ""
    i = 0
    
    while i < len(message):
        char = message[i]
        a = char in alphabet
        print(a)

main()