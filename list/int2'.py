# create a list of elemnts for a range of n even in ascending order and odd in descending order
n = int(input("Enter a number: "))
even = []
odd = []
for i in range(n+1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd.sort(reverse=True)
result = []
for i in range(n+1):
    if i % 2 == 0:
        result.append(even[i//2])
    else:
        result.append(odd[i//2])
print("Resultant list:", result)
# print even number in even index
#  and odd number in odd index

# convert it as set 
result_set = set(result)
print("Set of resultant list:", result_set)

# set differnace between the list end and prime number set 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
prime_set = []
for i in range(n+1):
    if is_prime(i):
        prime_set.append(i)
prime_set = set(prime_set)
print("prime_set", prime_set)
difference_set = result_set - prime_set
print("Difference between resultant set and prime set:", difference_set)