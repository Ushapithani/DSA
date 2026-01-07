def print_n_to_1(n: int) -> None:
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)