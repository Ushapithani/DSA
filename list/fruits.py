n = int(input("enter number of items:"))
list1=[]
for i in range(n):
    item = input("enter item")
    list1.append(item)
print(list1)
# length 
print("length of the list is:", len(list1))
# maximum
print("maximum item in the list is:", max(list1))
# minimum 
print("minimum item in the list is:", min(list1))
# sort
list1.sort()
print("sorted list is:", list1)