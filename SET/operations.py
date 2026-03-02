# all set operations
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}
print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = set1.difference(set2)

print("Difference (Set1 - Set2):", difference_set)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# accessing elements
print("Accessing elements in Set 1:")
for element in set1:
    print(element, end=' ')
print()

# Adding elements
set1.add(11)
print("Set 1 after adding 11:", set1)

# Removing elements
set1.remove(11)
print("Set 1 after removing 11:", set1)

# update
print("original Set 1:", set1)
set1.update({12, 13})
print("Set 1 after updating with {12, 13}:", set1)

# clear
print("Set 1 before clearing:", set1)
set1.clear()
print("Set 1 after clearing:", set1)

# remove all the even multiplies of 3 
for i in set1:
    if i % 2 == 0:
        set1.remove(i)
print("Set 1 after removing even multiples of 3:", set1)