import csv


# Part 4 (Optional)

# Write a program that creates and stores student grades.

# Your program should start by asking users whether they would like to add or view stored grades. If the user selects the first option, they should be repeatedly prompted for the names and module results (4CS001, 4CS015 and 4CI018) of students until the users enters a blank string, storing the information in a dictionary, before writing the data to a text file in JSON or CSV format.

# If the user selects to view student grades, any data stored in the results file should be read, loaded into a dictionary and presented to the user.

# Make sure to validate all inputs and utilise exception handling to avoid crashes.

def get_results():
    result_dic = []
    while True:
        module_name = input('Please enter module name: ')
        if module_name == '':
            break
        result = int(input(f'Please enter result for {module_name}: '))
        result_dic.append({'Module':module_name, 'Score':result})
    return result_dic

# one = get_results()
# print(one)

dictionary = get_results()

def dict_to_csv(dictionary):
    with open('scores_from_dict.csv', 'w') as file:
        fieldnames = ['Module', 'Score']
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        for x in dictionary:
            writer.writerow(x)
dict_to_csv(dictionary)

def csv_to_dic():
    with open('scores_from_dict.csv', 'r') as file:
        keys = ['Module', 'Score']
        reader = csv.DictReader(file, fieldnames= keys)
        for x in reader:
            print(x)

csv_to_dic()


# def main():

#     dict_result = get_results()
#     print(dict_result)

# if __name__ == main():
#     main()