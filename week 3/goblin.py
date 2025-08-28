import random
print("welcome to the goblin game")
print("THE BEST GAME EVER")
player_name = input("Write your name: ")
print(f"{player_name}, can you find the goblin")
print("|_|" * 15)
goblin_position = random.randint(1, 15)
keep_trying = True
while keep_trying:
    guess_position = int(input("can you guess where the goblin is? "))

    if goblin_position == guess_position:
        print("you won")
        keep_trying = False
    else: 
        print("NO")