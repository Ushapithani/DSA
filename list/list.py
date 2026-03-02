#create a list of alp for a range of n and convert it into set s1 which is alredy contains 1 3 5 7
n = int(input("Enter a number: "))
s = [1,3,5,7]
alp = []
for i in range(n):
    alp.append(chr(97+i))
print("List of alphabets:", alp)
result = s+alp
s1 = set (result)
print(s1)