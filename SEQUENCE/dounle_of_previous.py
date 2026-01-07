def print_sequence(n: int) -> None:
    value = 5
    result = []
    for i in range(n):
        result.append(str(value))
        value *= 2
    print(", ".join(result))

print_sequence(4)

# 5, 10, 20, 40