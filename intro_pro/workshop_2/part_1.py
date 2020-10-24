# importing the math module to use the factorial method
import math
from math import pi


#  The perimeter of a rectangle with length 9 and width 7

#  setting the values of the length and width for the rectangle
length = 9
width = 7

# setting the forluma for the perimeter of the rectangle and printing out the value
perimeter_rectangle = length * width
print(perimeter_rectangle)


# your name stored as a veriable

# using the veriable first_name and last_name to store my full name
first_name = 'mansoud'
last_name = 'mansouri'

# using the f-string to print the full name
print(f'{first_name} {last_name}')


# The maximun of 5, 2, -8, 9, 5.5, 7, and 0.

# placing the numbers in a list called numbers
numbers = [5, 2, -8, 9, 5.5, 7, 0]

# using the build in max() function/method to find the max number in the list
# assign it to veriable max_number
# print the max_number out

max_number = max(numbers)
print(max_number)



# Python is great, it's wild
# i will be using the \' to ignore/scape the inner '
#  it can also be done by single quote inside the double quite: "Python is great, it's wild"

wild_python = 'Python is great, it\'s wild!'
print(wild_python)



# The difference between Beth's age (57) and Tom's (34)
#  assigning their age to a veriable
Beth_age = 57
Tom_age = 34

# subtract the ages and assign it to another veribale and print the result
dif_bt_ages = Beth_age - Tom_age
print(dif_bt_ages)


# 2 to the 10th power
# evaluvating the result of 2 ** 10, assign it a veriable and printing the reslut out
two_power_ten = 2 ** 10
print(two_power_ten)


#  7 factorial minus 5 factorial
# using the fatorial function/method from the math module to evaluvate the result of 7! and 5!
# assing the result to a veriable
# subtract the  result and print out

seven_factorial = math.factorial(7)
five_factorial = math.factorial(5)

difference = seven_factorial - five_factorial
print (difference)


# Your forename multiplied by 5
# use the veriable last_name from above
# last_name * 5 will cancatinate the last name five times

five_last_name = last_name * 5
print(five_last_name)
# it does look nice

five_last_name_1 = f'{last_name} ' * 5
print(five_last_name_1)
# will make it look better and spaced out


# your name left justifies 15 spaces
# using the string rjust() and ljust() methods to give my name some padding
# the first argument is the number of white space and
# the second argument passed is the string that  will replace the white spaces

print(first_name.rjust(15, '*'))
print(first_name.ljust(15, '*'))

# pi to 5 decimal places
#  have to import pi from the maths module
# then use the round() function/method to round the result to 5 dp
# assing it to be veriable and print the thing out

pi_five_dp = round(pi, 5)
print(pi_five_dp)


# A veriable with the nake fed that stores the number 7
#  this one will through and error becuase def is a seversed keyword in Python

# 200 modules 12
# finding the modulo usnig the % operator, assign it to be veriable and print it out
remainder = 200 % 12
print(remainder)


#  7.2 as an integer value
print(type(7.2))

# 7.2 is a float and i will use int() function to covert it to a ingeter
int_seven = int(7.2)
print(int_seven)
print(type(int_seven))


#  the unicode encoding for your name
# using the string method encode()
# this will use python's defualt UTF-8 encoding, i think!

unicode_name = f'{first_name.encode()} {last_name.encode()}'
print(unicode_name)
