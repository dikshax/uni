# 1.  Write a program that opens and reads a text file and displays how many lines of text are in the file.
def num_lines():
    with open('original_text.txt', 'r') as file1:
        number_lines = 0
        file_list = file1.readlines()
        file_list = ' '.join(file_list)
        for x in file_list:
            if x == '\n':
                number_lines += 1
        return number_lines 

one = num_lines()
# print(one)



# 2.  Write a program that reads a text file named original_text, and writes every other line, starting with the first line, to a new file named new_text.

def other_line():
    with open('original_text.txt', 'r') as file:
        with open('new_text.txt', 'w') as file1:
            lines = file.readlines()
            for x in lines[:-1:2]:
                file1.write(x)
other_line()

# 3.  Write a program that reads a text file named original_text, and counts how many time the letter 'e' occurs (the most frequently occurring letter in English), and displays how many occurrences there are.

def finding_e():
    with open('original_text.txt', 'r') as file:
        list_line = file.readlines()
        words = ' '.join(list_line)
        i = 0
        for x in words:
            if x == 'e':
                i += 1
        return i

one = finding_e()
# print(one)

# 4. Write a program that reads a text file containing numerical expressions on each line and print them out along with the results. For example, for the numerical expression 4 + 2 in your file, your program should output: 4 + 2 = 6.

# def operations():
#     with open('numbers.txt', 'r') as file:
#         lines = file.readlines()
#         for x in lines:
#             first_num = x[0]
#             second_num = x[4]
#             sing = x[2]
#             result = first_num sing second_num
#             return result
