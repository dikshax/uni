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


# write a python function name check_quptes that is given a line read from a text file and returns True if each quote characters in the line has a matching quote (of the same type), othersive return False.


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
    one = 'this is a line'
    i = 0
    for x in one:
        
       print(x) 

two = count_letters()
print(two)