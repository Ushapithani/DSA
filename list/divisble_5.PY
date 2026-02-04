# CREATE  A LIST OF RANGE OF N NUMBER WHICH ARE DIVIDIBLE BY 5 AND REMOVE THE ODD NUMBERS
n = int(input("Enter the value of n: "))
numbers = list(range(1, n+1))
divisible_by_5 = []
for num in numbers:
    if num % 5 ==0:
        divisible_by_5.append(num)
print("Numbers divisible by 5:", divisible_by_5)
odd_numbers = []
for item in divisible_by_5:
    if item % 2 != 0:
        odd_numbers.append(item)
# remove odd numbers from the list
for odd in odd_numbers:
    divisible_by_5.remove(odd)
print("List after removing odd numbers:", divisible_by_5)