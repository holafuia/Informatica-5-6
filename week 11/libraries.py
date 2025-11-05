# import random

# coin = random.choice(["heads", "tails"])
# print (coin)

# number = random.randint(1, 10)
# print(number)

# cards = ["jack", "queen", "king", "ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import statistics
import sys
import cowsay
# print(statistics.mean([int(sys.argv[1]), int(sys.argv[2])]))

# print("Hello, my name is", sys.argv[1])

try:
    cowsay.trex(sys.argv[1])
except IndexError:
    sys.exit()