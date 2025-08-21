def main():
    x = int(input("write any number: "))
    so(x)

def so(q):
    if q >= 0:
        print(q)
    if q < 0:
        print(q * -1)

main()