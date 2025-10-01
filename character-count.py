def main():
    message = input("Write your message: ")
    count = {}
    dictionary(message, count)

def dictionary(message, count):
    for x in message:
        count.setdefault(x, 0)
        count[x] += 1
    for x in count:
        print(f"{x}: {count[x]}")
    
    print(f"The length is: {len(message)}")

    values = count[x]
    for y in count:
        value = count[y]
        if int(value) >= values:
            values = value
    maxs = []
    for a in count:
        value = count[a]
        if int(value) == values:
            maxs += a

    print(f"The letter(s) with most appearence are {maxs} with {values} letters each")

main()