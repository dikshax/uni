'''(a) write a Python program that prompts the user for two integer values and displays
the results of the first number divided by the second, with exactly two decimal places displayed.'''


# asking the user for the two numbers and store it in veriable number-1 and number_2
# int() is used to make sure the numbers are stored in integer format

number_1 = int(input('Please enter your first number: '))
number_2 = int(input('Please enter your second number: '))

# using the if statement to check if number_2 is zero, it cant be!
# if the number_2 is not zero, do the division and print the result

if number_2 == 0:
    print('Division by zero is not allowed!')

else:
    answer = number_1 / number_2
    print(f'{number_1} divided {number_2} equals to: {answer:.2f}')


'''(b) write a python program that prompts the user for two floating-point values and displays the
results of the first number divided by the second,  with exactly two decimal places displayed.'''

'''asking the user for two flaoting point number and store it in two distict veriable
float() method is used to make sure the input numbers are stored as flaoting point numbers'''

f_num_1 = float(input('Please enter your floating-point number one: '))
f_num_2 = float(input('Please enter your floating-point number two: '))

# # checking the type of the f_num_1
# # print(isinstance(f_num_1, float))

if f_num_2 == 0:
    print('Can\'t divide by zero!')
else:
    answer = f_num_1 / f_num_2
    print(f'{f_num_1} divided by {f_num_2} equals to: {answer:.2f}, to 2dp.')



'''(c) write a python program that prompts the user for two floating-point values and displays the
results of the first number divided by the second,  with exactly two decimal places displayed in scientific notation.'''

# this is the pretty much the same as task b, just putting out the answer in scietific notation

s_num_1 = float(input('Please enter your floating-point number one: '))
s_num_2 = float(input('Please enter your floating-point number two: '))

if s_num_2 == 0:
    print('Can\'t divide by zero!')
else:
    answer = s_num_1 / s_num_2
    print(f'{s_num_1} divided by {s_num_2} equals to: {answer:.2E}, to 2dp.')



''' (d) write a python program that prompts the user to enter a UTF-8 value between 32 and 126 and displays the corresponding charactor'''

# asking the user for the number
# checking if the number is the range 32-126
# printing out the carresponding charactor.

user_number = int(input('Please enter a number between 32 and 126: '))

if 32 > user_number or user_number > 126:
    print('the number entered is out of range!')
else:
    answer = chr(user_number)
    print(f'The UTF-8 corresponding charactor for {user_number} is {answer}')


''' (e) write a python program that allows the user to enter two integer values and displays the results of with the folowing arithmetic operators applied to them.'''

# ask the user for the two numbers
# apply all the operation on them
#  print them out

op_num_one = int(input('Please choose a number: '))
op_num_two = int(input('And the second number please: '))

ad_answer = op_num_one + op_num_two
sub_answer = op_num_one - op_num_two
mul_answer = op_num_one * op_num_two
div_answer = op_num_one / op_num_two
trun_div_answer = op_num_one // op_num_two
mod_answer = op_num_one % op_num_two
expo_answer = op_num_one ** op_num_two

print(f'Addition: {op_num_one} + {op_num_two} = {ad_answer}')
print(f'Subtraction: {op_num_one} - {op_num_two} = {sub_answer}')
print(f'Multiplication: {op_num_one} * {op_num_two} = {mul_answer}')
print(f'Division: {op_num_one} / {op_num_two} = {div_answer:.2f}')
print(f'Truncated Division: {op_num_one} // {op_num_two} = {trun_div_answer}')
print(f'Modulus: {op_num_one} % {op_num_two} = {mod_answer}')
print(f'Exponentiation: {op_num_one} ** {op_num_two} = {expo_answer:,}')


''' (f) all floating point results should be displayed with two decimal places of accuracy and with commas where appropriate'''

print(f'Addition: {op_num_one} + {op_num_two} = {ad_answer:,.2f}')
print(f'Subtraction: {op_num_one} - {op_num_two} = {sub_answer:,.2f}')
print(f'Multiplication: {op_num_one} * {op_num_two} = {mul_answer:,.2f}')
print(f'Division: {op_num_one} / {op_num_two} = {div_answer:,.2f}')
print(f'Truncated Division: {op_num_one} // {op_num_two} = {trun_div_answer:,.2f}')
print(f'Modulus: {op_num_one} % {op_num_two} = {mod_answer:,.2f}')
print(f'Exponentiation: {op_num_one} ** {op_num_two} = {expo_answer:,.2f}')



''' (g) write a version of the python program for qustion 5 above that performs all calculations using floating point values, regardless of wherether the user enters floating point values or not using explicit type conversion.'''

op_num_one = float(input('Please choose a number: '))
op_num_two = float(input('And the second number please: '))

ad_answer = op_num_one + op_num_two
sub_answer = op_num_one - op_num_two
mul_answer = op_num_one * op_num_two
div_answer = op_num_one / op_num_two
trun_div_answer = op_num_one // op_num_two
mod_answer = op_num_one % op_num_two
expo_answer = op_num_one ** op_num_two

print(f'Addition: {op_num_one} + {op_num_two} = {ad_answer}')
print(f'Subtraction: {op_num_one} - {op_num_two} = {sub_answer}')
print(f'Multiplication: {op_num_one} * {op_num_two} = {mul_answer}')
print(f'Division: {op_num_one} / {op_num_two} = {div_answer:.2f}')
print(f'Truncated Division: {op_num_one} // {op_num_two} = {trun_div_answer}')
print(f'Modulus: {op_num_one} % {op_num_two} = {mod_answer}')
print(f'Exponentiation: {op_num_one} ** {op_num_two} = {expo_answer:,2f}')
