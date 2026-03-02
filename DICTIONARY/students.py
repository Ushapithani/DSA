# create a dictionary to sstudents and delete last student 
students = {}
for i in range(1, 3):
    name = input(f"Enter the name of student {i}: ")
    students[i] = name
print("Students:", students)
# delete last student
del students[len(students)]
print("Students after deletion:", students)

# user can seletect which student to delete by entering the student number
student_number = int(input("Enter the student number to delete: "))
if student_number in students:
    del students[student_number]
    print("Students after deletion:", students)
else:
    print("Student number does not exist.")