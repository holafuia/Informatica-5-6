def main():

    thing = input("make a face 🙂 or ☹️ : ").strip().title()
    print(convert(thing))

def convert(to):
    return (to.replace(":)","🙂")
    .replace(":(","☹️")
    .replace(":", "Victor🗣️ 🗣️ 🗣️"))

main()