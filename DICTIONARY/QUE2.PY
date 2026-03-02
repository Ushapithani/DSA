# CRAETE A DICTIONARY NAME IT AS EMPLOYEE THE LIST OF KEYS ARE NAME, ADDRESS , COMPANY NAME  INSERT ATLEAST 3 EMPLOYEE DETAILS AND PERFORM UPDATE ON LAST EMPLOYEE SALARY AS 50000 TO 60000

# Create a dictionary named employee TAKE FROM USER INPUT
employee = {}
for i in range(1, 4):
    name = input("Enter the name of the employee: ")
    address = input("Enter the address of the employee: ")
    company_name = input("Enter the company name of the employee: ")
    salary = int(input("Enter the salary of the employee: "))
    employee[name] = {'address': address, 'company_name': company_name, 'salary': salary}
print("The employee details are:")
for name, details in employee.items():
    print({"Name": name, "Address": details['address'], "Company Name": details['company_name'], "Salary": details['salary']})
 # Update the salary of the last employee
last_employee = list(employee.keys())[-1]
employee[last_employee]['salary'] = 60000
print("The updated employee details are:")
for name, details in employee.items():
    print({"Name": name, "Address": details['address'], "Company Name": details['company_name'], "Salary": details['salary']})
# CRAETE A DICTIONARY OF FRUITS AND COSTS COMBINE WITH THE EMPLOYEE DICTIONARY
fruits = {"apple": 100, "banana": 50, "orange": 80}
employee['fruits'] = fruits
#print("The employee details with fruits are:")
#or name, details in employee.items():
    #print({"Name": name, "Address": details['address'], "Company Name": details['company_name'], "Salary": details['salary'], "Fruits": details['fruits']})
# UPDATE 
employee.update(fruits)
print("The updated employee details with fruits are:", employee)

# perform pop , del , clear

fruits.pop()
print(fruits)