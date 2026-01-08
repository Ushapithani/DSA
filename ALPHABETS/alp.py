n = int(input("Enter number of terms: "))

for i in range(n):
    ch = chr(ord('a') + i)
    print(ch * (i + 1))