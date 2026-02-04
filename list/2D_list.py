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