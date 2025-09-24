def main():
    matrix = [[3,5,8,2],[7,11,10,4],[2,8,5,9],[13,1,15,7]]
    for a in matrix:
        print(f"{a}\n")
    cal_rows(matrix)
    cal_columns(matrix)
    print("")
    change_matrix(matrix)

def cal_rows(matrix):
    select_row = int(input("put the desired row (0 to 3): "))
    sum = 0
    for x in matrix[select_row]:
        sum += x
    print(sum)
def cal_columns(matrix):
    select_column = int(input("put the desired column (0 to 3): "))
    sum = 0
    for y in matrix:
        sum += y[select_column]
    print(sum)
def change_matrix(matrix):
    rows = int(input("select the row (0 to 3): "))
    columns = int(input("select the number (0 to 3): "))
    the_change = int(input("insert the replacement number: "))
    matrix[rows][columns] = the_change
    for s in matrix:
        print(f"{s}\n")

main()