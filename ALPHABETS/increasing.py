# A
# A B
# A B C
# A B C D

for i in range(4):
    for j in range(i + 1):
        print(chr(ord('A') + j), end=' ')
    print()