def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def check_strong(number):
    total = 0
    temp = number
    
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    
    if total == number:
        print(number, "is a Strong Number")
    else:
        print(number, "is NOT a Strong Number")

num = int(input("Enter a number: "))
check_strong(num)