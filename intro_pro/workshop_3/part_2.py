'''define a function (types) that prints a given value both as a float and an integer'''

def types(num):
    if type(num) == int or type(num) == float:
        print(f'this is the number you have entered in INTEGER: {int(num)}')
        print(f'this is the number you have entered in FLOAT: {float(num)}')
    else:
        print('The argument passed to the function types is not a number, must be number to make it work!')

# print(types('this not gonna work')) # this will not work

# print(types(17))   # this will work no problem
# print(types(17.9)) # this will work tooo

#########################################################################################################################

'''define a function (Square) that take an inter and returns the value squared'''

def squared(num):
    if type(num) == int:
        return(f'{num} squared is: {num ** 2}')
    else:
        return(f'{num} is not a integer, please enter a ingeter number!')
result = squared(99)
# print(result)


#########################################################################################################################

'''define a function (int_to_string) that takes an interger value and returns it as a string'''

def int_to_string(num):
    if type(num) == int:
        return f'the string representation of {num} is: {str(num)}'
    else:
        return f'{num} is not a int type dude!'

result = int_to_string(13)
# print(result)


#########################################################################################################################

'''define a function (hello_world) that takes parameter anme and displays the following output to the console: "hello world, my name is name".'''

def hello_world(name):
    if type(name) == str:
        return f'Hello World, my name is {name.capitalize()}'
    else:
        return f'{name} is not a string!'

result = hello_world('mansoud')
# print(result)


######################################################################################################################

# define a function (print_ast) that takes an integer value n and a string symbol, with a defualt value of "*". this charater should be printed n times to the console.

def print_ast(num, symbol='*'):
    if type(num) == int:
        return f'{num * symbol}'
    else:
        return f'You this error because {num} is not a interger!'

result = print_ast(12)
# print(result)


###################################################################################################################

'''define a function (improved_average) that takes fice inter parameters. it should return the mode median and mean values of the numbers passred to the function.'''

# importing statistics to use some of the functions from it
import statistics

def improved_average(num0, num1, num2, num3, num4):
    numbers = num0, num1, num2, num3, num4
    print(f'The mode of {num0, num1, num2, num3, num4} is {statistics.mode(numbers)}')
    print(f'the median of {num0, num1, num2, num3, num4} is {statistics.median(numbers)}')
    print(f'The mean of {num0, num1, num2, num3, num4} is {statistics.mean(numbers)}')


# improved_average(5, 2, 2, 2, 5)



#######################################################################################################################

'''define a function (either_side) which when passes an inter value also prints the values which are one less and one more than that vlue.'''

def either_side(num):
    if type(num) == int:
        return f'You have entered {num}, one less than {num} is {num - 1}, one more than {num} is {num + 1}'
    else:
        return f'{num} is not integer, please enter a integer!!'


result = either_side(13)
# print(result)



###################################################################################################################

'''define a function (print_multiline_heading) that takes tow paeateterrs: name and years. it should output the following message using a single print statment.'''

def print_multiline_heading(name, years):
    if type(name) == str and type(years) == int:
        print(f'''
            Dear Feline Fanatic,
            Your cat has been arrested for:
                1. Catnapping
                2. Cat burglary
                3. Extortion.
            It will be sentenced to {years} years in prison.

            Sincerely, {name.capitalize()}
            ''')


print_multiline_heading('mansoud', 12)
