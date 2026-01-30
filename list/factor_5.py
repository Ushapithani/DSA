n = 50
multiples_of_7 = []

i = 1
while i <= n:
    if i % 7 == 0:
        multiples_of_7.append(i)
    i += 1

print(multiples_of_7)