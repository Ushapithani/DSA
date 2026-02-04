numbers = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]
even_list = []
odd_list = []

for num in numbers:
    if  num%7 ==0 and num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even multiples of 7:", even_list)
print("Odd multiples of 7:", odd_list)
# dynamic input

even_list = []
odd_list = []

for num in numbers:
    if num % 7 != 0:
        continue
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even multiples of 7:", even_list)
print("Odd multiples of 7:", odd_list)

# remove second element 
even_list.pop(1)
print("Even multiples of 7 after removing second element:", even_list)


# remove 21 

odd_list.remove(21)
print("Odd multiples of 7 after removing 21:", odd_list)

# remove even_list element
del even_list[:]
print("Even multiples of 7 after deleting all elements:", even_list)

# remove last element in the odd_list
odd_list.pop()
print("Odd multiples of 7 after removing last element:", odd_list)

# remove 2nd,3rd,4th elements in odd_list
del odd_list[1:4]
print("Odd multiples of 7 after removing 2nd, 3rd, and 4th elements:", odd_list)