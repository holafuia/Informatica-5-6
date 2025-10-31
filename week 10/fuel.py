def main():
    fuel()

def fuel():
    while True:
        try:
            fuel_level = input("write your fuel level as a fraction: ").split("/")
            x = fuel_level[0]
            y = fuel_level[1]
            z = (int(x)/int(y)) * 100
            if z == 100:
                print("F")
                break
            elif z == 0:
                print("E")
                break
            elif 0 < z < 100:
                print(f"{z}%")
                break
            else:
                print("Not Valid")
        except:
            print("Not Valid")

main()