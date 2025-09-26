def main():
    birthdays = {
        "Noemi": "09/12/2008",
        "Rodrigo": "10/09/2007",
        "Jefe Gabriel Alfa Omega Pro Max": "28/07/20008"
    }

    while True:
        name = input("Write the name you are searching for, press enter when empty to end program: ").title()
        if name == "":
            break
        if name not in birthdays:
            add = input("Sorry, that name is not in the list, would you like to add it? (yes or no): ").lower()
            if add == "no":
                continue
            if add == "yes":
                date = input("Please type the birthday date: ")
                birthdays[name] = date
                print("Add up completed")
        if name in birthdays:
            print(f"{name}'s birthday is in {birthdays[name]}")

    file = open("birthdays.txt", "w")
    for x in birthdays:
        file.write(f"{x}: {birthdays[x]}\n")
    
    file.close()

                

main()