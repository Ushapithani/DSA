# let us create an em,pty set called x and insert all the multiples of 3 for a range of n 
# craete another an empty set called y and insert all the multiples 6  for a range of n and 
#perfrom union , intersection , difference and symmetric difference operations on the two sets
n = 30
x = set()
y = set()
for i in range(n):
    if i%3 ==0 :
        x.add(i)
    if i %6 ==0:
        y.add(i)
print("Set x multiples of 3:", x)
print("Set y multiples of 6:", y)

# Union
union_set_x = x.union(y)
print("Union of x and y:", union_set_x)
# Intersection
intersection_set = x.intersection(y)
print("Intersection of x and y:", intersection_set)

# Difference
difference_set = x.difference(y)
print("Difference of x and y:", difference_set)

# Symmetric Difference
symmetric_difference_set = x.symmetric_difference(y)
print("Symmetric Difference of x and y:", symmetric_difference_set)