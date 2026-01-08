num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)
total = 0
for digit in num_str:
    total = int(digit)**power
if total == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")