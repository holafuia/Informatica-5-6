def number(so):
    return so.isnumeric()

def main():
    list = []
    while True:
        num = input("type a number for the list, 0 to exit: ")
        while not number(num):
            num = input("type a number for the list, 0 to exit: ")

        if num == 0:
            break
        list += num
        length(list)
        mean(list)
        range_of_list(list)

def length(x):
    print(len(x))

def mean(y):
    print("")

def range_of_list(a):
    largest = max(a)
    smallest = min(a)
    difference = int(largest) - int(smallest)
    print(f"the difference is: {difference}")

main()