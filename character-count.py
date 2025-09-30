def dictionary(message, count):
    for x in message:
        count[x] = +1
    for y in count:
        print(f"{y}: {count[y]}")

message = input("Write your message: ")
count = {}
dictionary(message, count)