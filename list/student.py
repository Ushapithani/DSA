# create a list of students marks of 15 students for a 50 marks test identify the stuents who got 1st ,2nd ,3rd 
# identify the list of falied students(less than 20 marks)
# find how many students got 42 marks 
# find how many students got same mark



# create a list of students marks of 15 students for a 50 marks test identify the stuents who got 1st ,2nd ,3rd 

marks = [23 , 23, 25 , 67 , 45 , 42 , 42 , 38 , 49 , 50 , 19 , 20 , 35 , 42 , 28 ]
for i in range(len(marks)+1) :
    marks_students = marks
    marks_students.append(marks)
    
print("Marks of students:", marks_students)

# studenrs who got 1st , 2nd and 3rd
sorted_marks = sorted(marks, reverse=True)
first = sorted_marks[0]
second = sorted_marks[1]
third = sorted_marks[2]
print("First highest mark:", first)
print("Second highest mark:", second)
print("Third highest mark:", third)

# identify the list of falied students(less than 20 marks)
failed_students = [mark for mark in marks_students if marks_students < 20]
print("Failed students less than 20 marks:", failed_students)

# find how many students got same mark
mark_count = {}
for mark in marks:
    if mark in mark_count:
        mark_count[mark] += 1
    else:
        mark_count[mark] = 1
print("Count of students with same marks:", mark_count)