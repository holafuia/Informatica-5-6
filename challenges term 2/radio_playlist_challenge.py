import time

weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
weekly_playlist.append("Drivers Licence")
weekly_playlist.insert(0, "Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")
print(weekly_playlist.index("Levitating"))
print(weekly_playlist.count("As It Was"))
weekly_playlist.reverse()
print(weekly_playlist)
weekly_playlist.sort()
print(weekly_playlist)
print(len(weekly_playlist))
print(weekly_playlist)

print("")
print("")
print("")
print("")
print("")
print("")
print("")

while True:
    print(weekly_playlist)
    weekly_playlist.append(weekly_playlist[0])
    weekly_playlist.remove(weekly_playlist[0])
    time.sleep(2)