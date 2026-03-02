# create a set contains list of 6 divisible numbers based on that craete a subsets of 2 divisibl and 3 divisible from that set 
n = int(input("Enter a number: "))
divisible_set = set()
for i in range(n+1):
    if i % 6 == 0:
        divisible_set.add(i)
print("Set of numbers divisible by 6:", divisible_set)
divisible_by_2 = set()
divisible_by_3 = set()
for num in divisible_set:
    if num % 2 == 0:
        divisible_by_2.add(num)
    if num % 3 == 0:
        divisible_by_3.add(num)
print("Subset of numbers divisible by 2:", divisible_by_2)
print("Subset of numbers divisible by 3:", divisible_by_3)