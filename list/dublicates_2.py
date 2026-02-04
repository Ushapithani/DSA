nums = [0,0,1,1,1,2,2,3,3,4]

unique_nums = []
for num in nums:
    if nums.count(num) >= 1 and num not in unique_nums:
        unique_nums.append(num)

print("Original list:", nums)
print("After removing duplicates:", unique_nums)


# print dublicates only 

numbers = [10, 20, 30, 40, 20, 30, 50, 60, 70, 80, 90, 100]

duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Original list:", numbers)
print("Duplicate elements:", duplicates)