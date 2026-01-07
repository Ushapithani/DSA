def print_sequence(n: int) -> None:
    value = 2
    power = 0
    result = [str(value)]
    for i in range(1, n):
        value += 2 ** power
        result.append(str(value))
        power += 1
    print(", ".join(result))

print_sequence(5)
 # 2, 3, 5, 9, 17