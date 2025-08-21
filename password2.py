import getpass

def main():
    password = getpass.getpass("Set password: ")
    input("press enter to log in")
    check_password(password)

def check_password(p):
    guess = input("enter password: ")
    if p == guess:
        print("Correct password")
    print("The program has ended.")

main()