# CREATE 1 TO 5 SQUARES USING DICTIONARY 
# 1 TO  N CUBES
# 1 TO  N EVEN 
# 1 TO N ODD

# Create a dictionary of squares from 1 to 5
squares = {i: i**2 for i in range(1, 6)}
print("The squares from 1 to 5 are:", squares)

# Create a dictionary of cubes from 1 to N
N = int(input("Enter the value of N for cubes: "))
cubes = {i: i**3 for i in range(1, N+1)}
print(f"The cubes from 1 to {N} are:", cubes)

# Create a dictionary of even numbers from 1 to N
N = int(input("Enter the value of N for even numbers: "))
even_numbers = {i: i for i in range(1, N+1) if i % 2 == 0}
print ("even number ", even_numbers)
# Create a dictionary of odd numbers from 1 to N
N = int(input("Enter the value of N for odd numbers: "))
odd_numbers = {i: i for i in range(1, N+1) if i % 2 != 0}

print("odd number ", odd_numbers)