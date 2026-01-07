def count_digits(n: int) -> int:
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
