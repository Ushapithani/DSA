def print_sequence(n: int) -> None:
    result = []
    num = 2
    for i in range(n):
        if i % 2 == 0:   
            result.append(str(num))
        else:            
            result.append(str(num * num))
            num += 1     
    print(", ".join(result))


print_sequence(7)

# 2, 4, 3, 9, 4, 16, 5