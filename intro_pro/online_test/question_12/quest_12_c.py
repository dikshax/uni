import csv

# # get the number of student you dealing with
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


def writing(filename, to_write):
    '''
    Will get a file name and write to it.
        Parameters:
            filename: name of the file to be created.
            to_write: the data you want to write
        Returns:
            NONE
    '''
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(to_write)

writing('test.csv', one)

def reading():
    '''
    Open and read the content of the file.
        Parameters:
            NONE
        Returns:
            content: the content of the file.
    '''
    content = []
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        for x in reader:
            content.append(x)
    return content

two = reading()
print(two)
