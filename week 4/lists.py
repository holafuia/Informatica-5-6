independence_stages = ["Inicio", "Organización", "Resistencia", "Consumación"]
print(independence_stages[0])
print(len(independence_stages))

#list methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(independence_stages) //mix lists together
leaders.insert(1, "José María Morelos")
#leaders.remove("Vicente Guerrero") //revomes things xd
leaders.append("Agustin de Iturbide")
#leaders.pop(1) //revomes things xd
#leaders.clear() //revomes all the list
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
#leaders.sort()
#leaders.reverse()
new_leaders = leaders.copy()

print(leaders)
print(new_leaders)