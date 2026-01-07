def print_sequence(n: int) -> None:
    value = 50
    result = []
    for i in range(n):
        result.append(str(value))
        value -= 5
    print(", ".join(result))

print_sequence(4)

# 50, 45, 40, 35