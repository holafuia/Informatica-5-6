def main ():
    check_password(input("password please: "))

def check_password(p):
    if p == "I've been in this games before":
        print("welcome back")
    if p != "I've been in this games before":
        y = input("WRONG!!, please try again: ")
        if y == "I've been in this games before":
            print("second try... how suprising")
        if y != "I've been in this games before":
            s = input("stop, hacking is not good, but try again: ")
            if s == "I've been in this games before":
                print("seriously, third try?")
            if s != "I've been in this games before":
                while True:
                    print("Stop " * 40)
                
main()