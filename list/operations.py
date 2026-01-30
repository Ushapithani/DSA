lst = [1, 2, 3]

print(lst[0])        # 1

print(lst[-1])       # 3

print(len(lst))      # 3

print(lst[0:2])      # [1, 2]

print(lst[::2])      # [1, 3]


lst.append(4)
print(lst)           # [1, 2, 3, 4]

lst.insert(1, 10)
print(lst)           # [1, 10, 2, 3, 4]

lst.extend([20, 30])
print(lst)           # [1, 10, 2, 3, 4, 20, 30]


lst.remove(10)
print(lst)           # [1, 2, 3, 4, 20, 30]

lst.pop()
print(lst)           # [1, 2, 3, 4, 20]

lst.pop(0)
print(lst)           # [2, 3, 4, 20]

del lst[1]
print(lst)           # [2, 4, 20]

lst.clear()
print(lst)           # []


lst = [1, 2, 3, 2, 4]

print(2 in lst)      # True

print(lst.index(3))  # 2

print(lst.count(2))  # 2


lst = [5, 2, 9, 1]

lst.sort()
print(lst)           # [1, 2, 5, 9]

lst.sort(reverse=True)
print(lst)           # [9, 5, 2, 1]

print(sorted(lst))   # [1, 2, 5, 9]

lst.reverse()
print(lst)           # [1, 2, 5, 9]

print(list(reversed(lst))) # [9, 5, 2, 1]


lst = [1, 2, 3]

copy1 = lst.copy()
print(copy1)         # [1, 2, 3]

copy2 = lst[:]
print(copy2)         # [1, 2, 3]


for x in lst:
    print(x)         # 1 \n 2 \n 3

for i, val in enumerate(lst):
    print(i, val)    # 0 1 \n 1 2 \n 2 3


lst = [1, 2, 3, 4]

print(sum(lst))      # 10

print(min(lst))      # 1

print(max(lst))      # 4


lst1 = [1, 2]
lst2 = [3, 4]

print(lst1 + lst2)   # [1, 2, 3, 4]

print(lst1 * 3)      # [1, 2, 1, 2, 1, 2]

