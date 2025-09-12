def number(so):
    return so.isnumeric()

def main():
    list = []
    while True:
        num = input("type a number for the list, 0 to exit: ")
        if number(num):
            num = int(num)
            if num == 0:
                break
            show(num, list)
            
        else:
            if ("-" in num) == True:
                num = num.replace("-", "")
                if number(num):
                    num = int(num)
                    num = num * -1
                    show(num, list)
                

def show(num, list):
    list.append(num)
    print(list)
    print(sorted(list))
    length(list)
    mean(list)
    range_of_list(list)

def length(x):
    print(f"the length is: {len(x)}")

def mean(y):
    print(round(sum(y)/len(y), 4))

def range_of_list(a):
    largest = max(a)
    smallest = min(a)
    difference = int(largest) - int(smallest)
    print(f"the difference is: {difference}")

main()