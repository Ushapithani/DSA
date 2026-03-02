# 2d list 
'''row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix = []
for i in range(row):
    matrix.append([])
    for j in range(col):

        value = int(input(f"Enter value for element ({i}, {j}): "))
        matrix[i].append(value)
print("2D List (Matrix):")'''


# create a 2d list  of n even numbers for i ,j rows and columns
'''n = int(input("Enter a number: "))
even_matrix = []
for i in range(n):
    even_matrix.append([])
    for j in range(n):
        if (i * n + j) % 2 == 0:
            even_matrix[i].append(i * n + j)
print("2D List of even numbers:", even_matrix)''


# create a 2d list  with perfect square numbers for i ,j rows and columns
n = int(input("Enter a number: "))
square_matrix = []
for i in range(n):
    square_matrix.append([])
    for j in range(n):
        square_matrix[i].append((i * n + j) ** 2)
print("2D List of perfect square numbers:", square_matrix)


# create a 2d list  of n even numbers for i ,j rows and columns


n = int(input("Enter a number: "))
even_matrix = []
for i in range(n):
    even_matrix.append([])
    for j in range(n):
        value = int(input(f"Enter value for element ({i}, {j}): "))
        if value % 2 == 0:

            even_matrix[i].append(value)
print("2D List of even numbers:", even_matrix)'''

# find the sum of elements in the 2d list find the count ,highest and lowest element in the 2d list
n = int(input("Enter a number: "))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        value = int(input(f"Enter value for element ({i}, {j}): "))
        matrix[i].append(value)

total_sum = 0
count = 0
highest = matrix[0][0]
lowest = matrix[0][0]
for i in range(n):
    for j in range(n):
        total_sum += matrix[i][j]
        count += 1
        if matrix[i][j] > highest:
            highest = matrix[i][j]
        if matrix[i][j] < lowest:
            lowest = matrix[i][j]
print("Sum of elements in the 2D list:", total_sum)
print("Count of elements in the 2D list:", count)
print("Highest element in the 2D list:", highest)
print("Lowest element in the 2D list:", lowest)