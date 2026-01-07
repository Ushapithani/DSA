def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def print_prime_squares(n: int) -> None:
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num * num)
            count += 1
        num += 1

#4 prime squares → 4, 25, 121, 289
print_prime_squares(4)