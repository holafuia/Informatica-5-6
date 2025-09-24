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
    row = matrix[select_row]
    sum = 0
    for x in row:
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
    row = matrix[rows]
    column = row[columns]
    change = input(f"the number is {column}, are you sure you want to change it? (yes or no): ").lower()
    if change == "no":
        for v in matrix:
            print(f"{v}\n")
    elif change == "yes":
        row.remove(column)
        the_change = int(input("insert the replacement number: "))
        row.insert(columns, the_change)
        matrix.remove(matrix[rows])
        matrix.insert(int(rows), row)
        for s in matrix:
            print(f"{s}\n")
    else:
        print(matrix)

main()