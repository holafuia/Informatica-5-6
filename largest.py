def main():
    length = int(input("Enter the desired length of the list: "))
    list = []
    
    for x in range(length):
        number = input("enter the numbers: ")
        file = open("largest.txt", "a")
        file.write(f"{number}\n")
        file.close()
        list += number
        
    print(max(list))
main()