n = 5
p = 65
for i in range(n):
    for j in range(i+1):
        print(chr(p), end=' ')
    p += 1
    print()
'''
A
B B
C C C
D D D D
E E E E E'''