thing = input("make a face 🙂 or ☹️ : ").strip()
thing = thing.replace(":)","🙂")
thing = thing.replace(":(","☹️")
print(thing)