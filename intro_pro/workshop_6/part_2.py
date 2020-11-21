import random


# 1. write a python function called reduce_space that is given a line read from a test file and trutns the line with all extra space chractors removed.

def reduce_spaces():
    '''
    return the file with all the extra white spaces removed.
    
    -- split() will split a string into list where every word is a list item.

    -- join() take all the items in an iterable and joins them into one string.
    '''
    with open('spaced.txt', 'r') as with_space:
        one = with_space.readlines()
        one = ' '.join(one)
        no_extr_space = one.split()
        no_extr_space = ' '.join(no_extr_space)
        print(no_extr_space)
#reduce_spaces()


# 2. write a python function named extra_temp that is given an line read from a text file and displays the one number (ingeter) found in the string.

def extract_temp():
    with open('extract_temp.txt', 'r') as file:
        list_file = file.readlines()
        one = ' '.join(list_file)
        one = one.split()
        for x in one:
            if x.isdigit():
                print(x)
#extract_temp()


# 3. write a python function name check_quptes that is given a line read from a text file and returns True if each quote characters in the line has a matching quote (of the same type), othersive return False.


def check_quotes():
    with open('check_quote.txt', 'r') as file:
        content = file.readlines()
        content = ''.join(content)

        ii = 0
        i = 0
        for x in content:
            if x == '\'':
                i += 1
            elif x == '"':
                ii += 1
        if i % 2 == 0 and ii % 2 == 0:
            return True
        else:
            return False
           
#one = check_quotes()
#print(one)    


# 4.  Write a Python function named count_letters that is given a line read from a text file and returns a list containing every letter in the line and the number of times that each letter appears (with upper/lower case letters counted together)
# ‘This is a line’ → [ (‘t’, 1), (‘h’, 1), (‘i’, 3), (‘s’, 2), (‘a’, 1), (‘l’, 1), (‘n’, 1), (‘e’, 1) ]

def count_letters():
    pass


# 5.  Write a Python function named interleave_chars that is given two lines read from a text, and returns a single string containing the characters of each string interleaved: ‘Hello’, ‘Goodbye’ → ‘HGeololdobye’

def interleave_chars(word):
    pass

# 6. Give a for loop that counts all the characters in a string assigned to variable line, except blanks and the newline character. 

def character():
    pass



# 7. For variable month which contains the full name of any given month, give an expression to display just the first three letters of the month.

def month(month):
    first_3 = month[:3]
    return first_3

one = month('October')
# print(one)

# 8. Give an expression that displays True if the letter ‘r’ appears in a given month name stored in variable month, otherwise displays False.

def have_r(month):
    if 'r' in month:
        return True
    else:
        return False
one = have_r('october')
# print(one)

# 9. Give an expression for determining how many times the letter ‘r’ appears in a given month name stored in variable month.

def letter_r(month):
    i = 0
    for x in month:
        if x == 'r':
            i += 1
    return f'There is {i} \'r\' in {month}'

one = letter_r('october')
# print(one)


# 10. For a person’s first name stored in variable first_name, and last name stored in variable last_name, give an expression that displays the person’s name formatted exactly as follows: Jones, William.

def full_name():
    first_name = input('please enter first name: ')
    second_name = input('please enter your second name: ')

    full = f'{first_name.capitalize()}, {second_name.capitalize()}.'
    return full

# one = full_name()
# print(one)


# 11. Give an instruction that determines if a given social security number represented as a string and stored in variable ss_num, contains any non- digits. 

def non_digit(ss_num):
    pass

# 12. Give an instruction that determines the index of the ‘@’ character in an email address stored in variable email_addr.


def finding(email_addr):
    for x in email_addr:
        if x == '@':
            return email_addr.index(x)
            

one = finding('manny@')
# print(one)


# 13. For a variable named date containing a date in the form 12/14/2012, give an expression that replaces all slashes characters with dashes.

def date_format(date):
    new_date = ''
    for x in date:
        if x == '/':
            new_date += x.replace('/', '-')
        else:
            new_date += x
    return new_date

one = date_format('21/12/1212')
# print(one)


# 14. For a variable named err_mesg that contains error messages in the form ** error message **, give an expression that produces a string containing the error message without the leading and trailing asterisks and blank characters.

def error(message):
    new_message = ''
    for x in message:
        if x == '*':
            continue
        else:
            new_message += x
    return new_message

one = error('** error message **')
# print(one)


