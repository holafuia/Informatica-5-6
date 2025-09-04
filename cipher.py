def main():
    #put an input
    message = input("write a message: ").lower()
    #run the encode_message def
    encode_message(message)

def encode_message(message):
    #the alphafet right and backwards
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    #new_message is empty because there's where the message with be stored
    new_message = ""
    #i to identify the specific text character
    i = 0
    
    #while to loop until i is greater
    while i < len(message):
        #char is equal to the chosen character
        char = message[i]
        
        #the if so it only counts alphabet letters
        if char in alphabet:
            #this is to find where the character is in the alphabet function
            cipher_index = alphabet.find(char)
            #this will add the cipher character to the new_message. the programs nows what to put because cipher_index knows the location of the past alphabet character
            new_message += cipher[cipher_index]
            # both (the else and the other thingie) are just to ignore other thing that are not alphabet characters
        else:
            new_message += char
        #this adds 1 to i so we don't get stuck in the loop and to change the character in the cipher_index
        i += 1
    #it prints xd
    print(new_message)

main()