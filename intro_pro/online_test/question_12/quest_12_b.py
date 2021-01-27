# get the number of student you dealing with
try:
    num_student = int(input('Please enter the number of students to creade record for: '))
except ValueError as r:
    print('Please check you enter a whole number for the number of students!')

# getting student name and id, store it  in a list
# getting modules grade and store it in a dictionary
# combining the list and dictionary into one students list
def getting_info(num_student):
    '''
    Get infor mation for x number of students.
        Parameters:
            num_student: number of student to create record for.
        Returns:
            Studentz: a list containg all the info for all the students.
    '''
    try:
        studentz = []
        for x in range(1, num_student + 1):
            one_student = []
            module_grades = {}
            
            ID = input(f'Please enter the ID for student number {x}: ')
            name = input(f'Please enter the name of student number {x}: ')
            one_student.append(ID)
            one_student.append(name)
            cs1 = int(input(f'Enter 4CS001 grade for student {x}: '))
            module_grades.update({'4CS001':cs1})
            cs5 = int(input(f'Enter 4CS005 grade for student {x}: '))
            module_grades.update({'4CS005': cs5})
            cs8 = int(input(f'Enter 4C1018 grade for student {x}: '))
            module_grades.update({'4CS1018': cs8})
            one_student.append(module_grades)

            studentz.append(one_student)
        return studentz
    except ValueError:
        print('Please check your input values!!!')
one = getting_info(num_student)


# statics for module 4CS001
grades_001 = []
for x in one:
    grade = x[2]['4CS001']
    grades_001.append(grade)

highest = max(grades_001)
print(f'The highest grade for module 4CS001 is: {highest}')

lowest = min(grades_001)
print(f'The lowest grade for module 4CS001 is: {lowest}')

average = round(sum(grades_001) / len(grades_001), 2)
print(f'The average of the grades is: {average} in 2dp.')

# static for module 4CS005
grades_005 = []
for x in one:
    grade = x[2]['4CS005']
    grades_005.append(grade)

highest = max(grades_005)
print(f'The highest grade for module 4CS005 is: {highest}')

lowest = min(grades_005)
print(f'The lowest grade for module 4CS005 is: {lowest}')

average = round(sum(grades_005) / len(grades_005), 2)
print(f'The average grade for the module is: {average} in 2dp.')

# statics for module 4CS1018
grades_008 = []
for x in one:
    grade = x[2]['4CS1018']
    grades_008.append(grade)

highest = max(grades_008)
print(f'The highest grade for module 4CS005 is: {highest}')

lowest = min(grades_008)
print(f'The lowest grade for module 4CS005 is: {lowest}')

average = round(sum(grades_008) / len(grades_008), 2)
print(f'The average grade for the module is: {average} in 2dp.')