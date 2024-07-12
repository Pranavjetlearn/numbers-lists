table = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
count = 0
for row in table:
    for element in row:
        count += element

print(count)
for row in table:
    for number in row:
        print(number)

print("\n")
rows = int(input("how many rows do you want"))
colums = int(input("how many colums do you want"))

matrix = []
for i in range(rows):
    row = []
    for j in range(colums):
        element = int(input(f"enter element at position({i}{j})"))
        row.append(element)
    matrix.append(row)
for row in matrix:
    print(row)