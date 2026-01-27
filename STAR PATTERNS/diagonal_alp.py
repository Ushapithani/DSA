n = 5
for i in range(n):
    row = []
    for j in range(n):
        if i==j:
            row.append(chr(65+i))
        else:
            row.append("*")
    print(" ".join(row))
'''
A * * * *
* B * * *
* * C * *
* * * D *
* * * * E
'''

# diagonal reverse alp pattern 
n = 5
for i in range(n):
    row = []
    for j in range(n):
        if i+j==n-1:
            row.append(chr(65+i))
        else:
            row.append("*")
    print(" ".join(row))


'''''
* * * * A
* * * B *
* * C * *
* D * * *
E * * * *
'''

# cross diagonal

n = 5
for i in range(n):
    row = []
    for j in range(n):
        if i==j or i+j==n-1:
            row.append(chr(65+i))
        else:
            row.append("*")
    print(" ".join(row))

'''A * * * A
* B * B *
* * C * *
* D * D *
E * * * E
'''