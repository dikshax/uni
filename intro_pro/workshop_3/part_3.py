'''1. create a function that prompts the user for two integer balues and displys the results of the first number divided by the second to two decimal places.'''

def division(num0, num1):
    ''' this is a fucntion that will take two integer number as arguments.
        the function will devide the first argument by the second argument
        and the result will be returned in 2 decimal places '''
    if type(num0)== int and type(num1) == int:
        return f'{num0} divided by {num1} is: {round(num0 / num1, 2)}, to two decimal places.'
    else:
        return 'make sure you inter two integer numbers as your arguments!'


result = division(13, 6)
# print(result)


######################################################################################################################

'''create a python program called calculator with functions to perform the following arithmatic calculations, each should take two decimal parameters and return the result of the arithmetic calculation in question.'''

def calculator(num0, num1):
    ''' this function will take two floating point numbers as the parameters, the following calculation will be carried on the passed in arguments: addistion, subtraction, multiplication, division, truncated disision, modolus and exponentiation. all the answers are returned with 2 decimal places. '''

    if type(num0) == float and type(num1) == float:
        return f'''
        Addition: {num0} + {num1} = {num0 + num1 :.2f}
        Subtraction: {num0} - {num1} = {num0 - num1 :.2f}
        Multiplication: {num0} x {num1} = {num0 * num1 :.2f}
        Division: {num0} / {num1} = {num0 / num1:.2f}
        Truncated division: {num0} // {num1} = {num0 // num1 :.2f}
        Modulus: {num0} % {num1} = {num0 % num1 :.2f}
        Exponentiation: {num0} ** {num1} = {num0 ** num1:.2f}
        '''
    else:
        return 'The arguments passed to this functions MUST  be decimal numbers!'

result = calculator(12.77, 7.99)
# print(result)

#################################################################################################################
'''Go back and add multi-line docstrings to each of the fundtions you defined in the previous question. use the help function to check them afterwards.'''

# print(help(division))
# print(help(calculator))


####################################################################################################################
''' download the file broken_code from canvas. the file conteains several errors, your task is to fix theis code to that it rurns without issues.'''


# print("Let's practice everything.")
# print('You\'d need to know about escapes charactors with \\ (back-slash), \\n will create a  newline and \\t do tab.')


poem = """The lovely world
with logic so firmly planted
cannot discern
the needs of love
nor comprehend passion from intuition
and requires an explantion
where there is none."""
# print(poem)


def print_heading(text, sep='-'):
    '''This function will print a nice heading.'''
    print(sep * 15)
    print(text)
    print(sep * 15)
    print('Hello World')
    print(sep * 15)

# print_heading(poem)


five = 10 - 5
# print("This should be five: {0}".format(five))


def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(8, 5)
# print(result)



def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, crates

start_point = 10000
result = secret_formula(start_point)
# print(result)


start_point = start_point / 10
# print("We can also do that this way:")
# print("We'd have {0} beans, {2} jars, and {1} crabapples.".format(secret_formula(start_point)))



sentence = "All good things come to those who wait."

# print(sepentence)
