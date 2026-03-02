# create a dictionary  of students  as a nested dictionary for every name of student dictionary of subjects and marks
students = {}
for i in range(1, 3):
    name = input(f"Enter the name of student {i}: ")
    subjects = {}
    for j in range(1, 4):
        subject = input(f"Enter the name of subject {j} for student {name}: ")
        marks = int(input(f"Enter the marks for {subject}: "))
        subjects[subject] = marks
    students[name] = subjects
print("Students and their subjects with marks:", students)
