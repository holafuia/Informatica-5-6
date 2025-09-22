# names = ["Bob", "Alex", "Kevin"]
# names.append("Joseph")

# for name in sorted(names):
#     print(name)

#list with floats
# measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
# mean = sum(measurements)/len(measurements)
# print(f"the measure is: {mean}")

#list within lists
# super_list = [[5,2,3],[4,1],[2,2,5,1]]
# print(super_list[1])

# grades = [["Shanclas",8,"D"],["La agresiva",0,"C"],["Shensi",10,"A"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     group = student[2]
#     print(f"{name} from group {group} got a {grade}")

#Matrices
matrix = [[1,2,3],[4,5,6],[7,8,9]]
list = []
#print rows
i = 0
while i != 3:
    for row in matrix:
        list.append(row[i])
    print(list)
    list.clear()
    i += 1