# all list operations
original = [2,3,4,5,6,7,8,8,65,43]
elements =[]
for i in original :
    # append 
    elements.append(i)
print(elements)
# insert
elements.insert(2,10)
print(elements)
# extend
elements.extend([20,30,40])
print(elements)
# remove (value)
elements.remove(10)
print(elements)
# pop (index)
elements.pop()
print("After popping last element:")
elements.pop(0)
print("after removing 0th elemnet",elements)
# delete (index)
del elements[1]
print("After deleting index 1:",elements)
# delete range
del elements[1:3]
print("After deleting range 1 to 3:",elements)
# clear
elements.clear()
print("After clearing the list:",elements)
# re-initialize list
re_initialze = [2,3,4,5,6,7,8,8,65,43]
# index # value
re_initialze.index(65)
print("Index of value 65:", re_initialze.index(65))