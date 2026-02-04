# create a list of students marks of 15 students
marks = [2, 45, 78, 78, 34, 23, 45, 67, 89, 12, 34, 56, 78, 90, 42]

marks_students = marks.copy()  

print("Marks of students:", marks_students)

# identify 1st, 2nd, 3rd 
sorted_marks = sorted(marks_students, reverse=True)

first = sorted_marks[0]
second = sorted_marks[1]
third = sorted_marks[2]
print("First highest mark:", first)
print("Second highest mark:", second)
print("Third highest mark:", third)

# identify failed students (less than 20)
failed_students = []
for mark in marks_students:
    if mark < 20:
        failed_students.append(mark)

print("Failed students less than 20 marks:", failed_students)

# count students who got 42 marks
count_42 = marks_students.count(42)
print("Number of students who got 42 marks:", count_42)
 
repeated_numbers = []

for mark in sorted_marks:
    if sorted_marks.count(mark) > 1 and mark not in repeated_numbers:
        repeated_numbers.append(mark)
        print(f"Mark {mark} is repeated {sorted_marks.count(mark)} times")

