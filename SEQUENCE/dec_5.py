def print_sequence(n: int) -> None:
    result = []
    for i in range(n):
        result.append(str(50 - i * 5))
    print(", ".join(result))

# Driver code
print_sequence(4)