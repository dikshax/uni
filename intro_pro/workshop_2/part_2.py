# 1. Give the following values in the exponential notation of Python, such that there is only one
# significant digit to the left of the decimal point.

# (a)4580.5034    (b)0.00000046004     (c)5000402.000000000006
a = 4580.5034
number_1 = '{:E}'.format(a)
print(number_1)


b = 0.00000046004
number_2 = '{:E}'.format(b)

print(number_2)


c = 5000402.000000000006
number_3 = '{:E}'.format(c)
print(number_3)


# use the format function to display the flowating-point value in variable result with three decimal digits of precision

result = format(a, '.2f')

# or you can do the same thing with f-string (only in python 3 and above)
result_0 = f'This is the veriable  a in two decimal places: {a:.2f}'

print(result)
print(result_0)

result_1 = f'This is the veriable b in 2 decimal places: {b:.2f}'
print(result_1)

result_2 = f'This is the veriable c in 2 decimal places: {c:.2f}'
print(result_2)


# Give a modefies version of the format funstion in (a) so that commas are included in the dispalyed result
result = f'This is the veriable a with commas: {a:,.2f}'
print(result)


result_1 = f'This is the veriable b with commas, well not really!: {b:,.2f}'
print(result_1)

result_2 = f'This is the veriable c with commas: {c:,.2f}'
print(result_2)


# give a call to print that is provided one string that displays the following address on three sepatrat lines:
'''
John Doe
123 Dudley Street
Wolverhampton, Werst Midlands, WV1 4BF
'''
# will use the triple quotations to print multi-line context
print(''' John Doe
123 Dudley Street
Wolverhampton, Werst Midlands, WV1 4BF''')


# Reagarding variable assignment

# (a) what is the value of the vatiavle num after the following is excuted?

k = 5
num = 0
num1 = num + k * 2
num2 = num + k * 2

# yeah the value of the veriable num will not change
# the variable num is used to evaluate the values of num1 and num2 but itself does not change
print(num)

# (b) are the values id(num1) and id(num2) equal after the last statement?
# given that:
num1 = num + k * 2
num2 = num + k * 2

# they will have the same value, one object with two labels!
# num1 and num2, both pointing at the same memory address

print( f'num1 equals to: {num1} and num2 will be the same: {num2}')
print(f'and the id of num1 is: {id(num1)} and the id of num2 is: {id(num2)}, which is the same.')

# double check
same_id = {id(num1)} == {id(num2)}
print(same_id)



# 5. regarding the build-in input() function in Python
#  (a) give an instruction that prompts a user for their last name and stores it in a variable name last_name.

last_name = input('Please enter your lastname mate: ')
print(f'hello there {last_name.capitalize()}, you handsome beast :)')

# (b) give an instruction that prompts a user for their age and stores it as an integer in a variable name age.

age = int(input('Please dude enter your age: '))
print(f'so your last name is {last_name.capitalize()} and your {age} years old. interesting!')

# making sure that the veriable age is storing integer and not string
test_age = type(age)
print(test_age)

# double insanity check
print(isinstance(age, int))


# (c) give an instruction that prompts a user for their temperature and stores it as a float in a variable
#  named current_temperature.

current_temperature = float(input('Dude you forgot to tell me your temperature: '))
person = f'lastname: {last_name}, age: {age}, temperature: {current_temperature}C'

print(f'here is some info that you have entered: {person}')
