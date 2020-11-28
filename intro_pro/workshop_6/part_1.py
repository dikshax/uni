# 1.  create a program in python that opens a file named 'datafile.txt' for reading and assigns idenfier input_file to the file object created.

with open('datafile.txt', 'r') as input_file:
    pass

# 2. create a program in python that opens a file named 'datafile2.txt' for writing and assigns identifier output_file to the file object created.

with open('datafile2.txt', 'w') as output_file:
    pass


# 3. assume that input_file is a file object for a text file open for reading, and output_file is a file object for a text file open for writing. explain the content fo the output after the following code terminates:
    '''
    empty_str = ''
    line = input_file.readline()
    while line != empty_str:
        output_file.write(line + '\n')
        line = input_file.readline()
    '''

with open('datafile.txt', 'r') as input_file:
    with open('datafile2.txt', 'w') as output_file:
        empty_str = ''
        line = input_file.readline()
        while line != empty_str:
            output_file.write(line + '\n')
            line = input_file.readline()


# 4. identify the error in the folowing code:
    '''
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter file name: ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except:
            print('Input file not found')
    '''
    
'''
the peace of code was not indented properly. the code was not indented for the while block and also inside the except clause. the rest looks ok to me!
'''

input_file_opened = False
while not input_file_opened:
    try:
        file_name = input('Enter file name: ')
        input_file = open(file_name, 'r')
        input_file_opened = True
        input_file.close()
    except:
        print('Input file not found')

