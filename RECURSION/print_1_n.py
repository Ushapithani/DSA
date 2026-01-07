def print_1_to_n(n: int) -> None:
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)