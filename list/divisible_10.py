numbers = list(range(10, 101, 10))
print("Original list:", numbers)

numbers.pop()
print("After removing first element:", numbers)

numbers.pop(3)
print("After removing 3rd element:", numbers)

print("1st to 4th elements:", numbers[0:4])

pos = numbers.index(30)
print("Position of 30:", pos)