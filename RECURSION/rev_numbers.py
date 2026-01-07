def reverse_number(n: int, rev: int = 0) -> int:
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)