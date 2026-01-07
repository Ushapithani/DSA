def print_sequence(n: int) -> None:
    result = []
    for i in range(1, n + 1):
        result.append(str(9 * i))
    print(", ".join(result))

print_sequence(4)

# 9, 18, 27, 36