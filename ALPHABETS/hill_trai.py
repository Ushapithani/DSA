n = 5
for i in range(n):
    for j in range(i, n - 1):
        print(' ', end=' ')
    
    p = 65
    for j in range(2 * i + 1):
        print(chr(p), end='')
        p += 1
    print()