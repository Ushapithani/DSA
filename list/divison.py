n = int(input("Enter the limit: "))

for i in range(1, n+1):
    if (i % 5 == 0) and (i % 2 == 0 or i % 6 == 0):
        print(i, end=" ")