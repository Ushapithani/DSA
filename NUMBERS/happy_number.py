def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def check_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    if num == 1:
        print("Happy Number")
    else:
        print("Not a Happy Number")

n = int(input("Enter a number: "))
check_happy(n)