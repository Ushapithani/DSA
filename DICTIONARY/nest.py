# craete a nested dictionary of employees name containes dictionary of office name and salary


employees = {}

num_employees = int(input("Enter number of employees: "))

for i in range(num_employees):
    print(f" Employee {i+1} ")
    name = input("Enter employee name: ")
    office = input("Enter office location: ")
    salary = int(input("Enter salary: "))
    
    employees[name] = {
        "office": office,
        "salary": salary
    }

print("Final Employees Dictionary:")
print(employees)