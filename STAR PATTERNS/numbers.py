# floyd traingle 
n = 5
num = 1
for i in range(1,n+1):
    row = []
    for j in range(1,i+1):
        row.append(str(num))
        num += 1
    print(" ".join(row))
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15'''

# pascal traingle
n = 5
for i in range(n):
    print(" "*(n-i), end="")
    val = 1
    row = []
    for j in range(i+1):
        row.append(str(val))
        val = val*(i-j)//(j+1)
    print(" ".join(row))

'''  1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
'''
# palindrome number 
n = 4
for i in range(1,n+1):
    left = "".join(str(j) for j in range(1,i+1))
    right = "".join(str(j) for j in range(i-1,0,-1))
    print(left+right)
'''
1
121
12321
1234321
'''
