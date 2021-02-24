# asking the user for the number of student/s
try:
    num_students = int(input('Please enter the number of student you want to make a record for: '))
except ValueError:
    print('Number of student must be a whole number!!')

# looping over the number of students entered and getting the details for each
# make a list for each student
# make a list for all the student's lists

try:
    students = []
    for x in range(1, num_students + 1):
        one_student = []
        ID = input(f'Please enter the id for student {x}: ')
        name = input(f'Please enter the name for student number {x}: ')
        grade =int(input(f'Please enter the grade for student number {x}: '))
        one_student.append(ID)
        one_student.append(name)
        one_student.append(grade)
        students.append(one_student)
except ValueError as v:
    print('Please make sure ID and name is entered as text and grade as number!!')

# making a list of all the grades
grades_list = [] 
for x in students:
    grade = x[2]
    grades_list.append(grade) 

# working the highest grade with for loop
maximum = grades_list[0]
for x in grades_list:
    if x > maximum:
        maximum = x
#print(maximum)

# It also can be done easily with max() build in function
maximum = max(grades_list)
print(f'The highest grade in the list is: {maximum}')

# working the minimum values amongs the grades with min() build in function
minimum = min(grades_list)
print(f'The lowest grade in the list is: {minimum}')

# findin the average by using the sum() and len() build in functions
average = round(sum(grades_list) / len(grades_list), 2)
print(f'The average of the grades is: {average}')


