import time
def number(so):
    return so.isnumeric()

while True:
    x = input("Write 1, 2, 3, 4, or 5 to motivate (not 6): ")
    while not number(x):
        x = input("Write 1, 2, 3, 4, or 5 to motivate (not 6): ")
        
    if int(x) == 1:
        while True:
            print("Trust In The Lord In Every Time")
            time.sleep(1)
    elif int(x) == 2:
        while True:
            print("Todo Pasa Por Una Razón")
            time.sleep(1)
    elif int(x) == 3:
        while True:
            print("A Despertarse Mi Amor")
            time.sleep(0.1)
    elif int(x) == 4:
        while True:
            print("Time to read :)")
            time.sleep(0.5)
    elif int(x) == 5:
        while True:
            print("Time to think about life")
            time.sleep(5)
    elif int(x) == 6:
        while True:
            print("LET´S PLAY SOME CLASH ROYALE  " * 7)
    else:
        print("sorry buddy, not valid")