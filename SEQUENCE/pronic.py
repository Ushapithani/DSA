def print_pronic_numbers(n: int) -> None:
    for i in range(1, n + 1):
        print(i * (i + 1), end=' ')

print_pronic_numbers(5)