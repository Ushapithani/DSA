n = 5  # odd number of rows

# Top half (includes middle row)
for i in range(1, n//2 + 2):
    left = "*" * i
    space = " " * (n - 2*i)
    right = "*" * i
    print( left+ space+right)

# Bottom half
for i in range(n//2, 0, -1):
    left = "*" * i
    space = " " * (n - 2*i)
    right = "*" * i
    print(left + space + right)