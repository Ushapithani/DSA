# A
# B B
# C C C

for i in range(3):  
    ch = chr(ord('A') + i)  
    for j in range(i + 1):  
        print(ch, end=' ')
    print()