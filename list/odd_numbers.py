odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
less_than_10 = []
for num in odd_numbers:
    if num % 2 == 1 and num < 10:   
        less_than_10.append(num)
        print(num, end=" ")
less_than_10_slice = odd_numbers[:5]
print("Using slicing:", less_than_10_slice)

