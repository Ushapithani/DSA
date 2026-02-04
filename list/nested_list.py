# create nested list using loops
nested_list = []
for i in range(3):
    inner_list = []
    for j in range(4):
        inner_list.append(i + j)
    nested_list.append(inner_list)
print("Nested List:", nested_list)


# 2d list 
# create 2D list
rows = 3
cols = 4
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix.append(row)
print("2D List (Matrix):", matrix)
