
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match choice:
    case '1':
        result = num1 + num2
        print("Result:", result)
    case '2':
        result = num1 - num2
        print("Result:", result)
    case '3':
        result = num1 * num2
        print("Result:", result)
    case '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2   
            print("Result:", result)
    case _:
        print("Invalid input")