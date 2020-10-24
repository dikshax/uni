# Evaluate the following expressions

num1= 10
num2 = 20

expressions_1 = not (num1 < 1) and num2 < 10
print(expressions_1)

# expressions_2 = not (num1 < 1) and num2 < 10 or num1 + num3 < 100
#not going to work cuase num3 is not defined dude

expressions_3 = not(num2 > 1) or num1 > num2 - 10
print(expressions_3)


# 2. give an aropriate if statement for each of the following
# a. Display 'whtin range' if num is between 0 and 100, inclusive

num = -123
if 0 <= num <= 100:
    print(f'yeah, {num} is within the range of 0-100!')
else:
    print(f'{num} is not in range of 0-100')

# b. Displays 'within range' if num is between 0 and 100, inclusive, and displays 'out of range' otherwise.

if 0 <= num <= 100:
    print(f'{num} is within the range')
else:
    print(f'{num} is out of range')


# 3. rewrite the follwing if-else statements using a single if statement and elif:

tempreture = 121
humidity = 65
'''
if tempreture >= 85 and humidity > 60:
    print('muggy day today')
else:
    if tempreture >= 85:
        print('warm, but  not muggy today')
    else:
        if tempreture >= 65:
            print('pleasant today')
        else:
            if tempreture <= 45:
                print('cold today')
            else:
                print('cold')
'''

if tempreture >= 85 and humidity > 60:
    print('muggy day today')
elif tempreture >= 85:
    print('warn, but not muggy today')
elif tempreture >= 65:
    print('pleasant today')
elif tempreture <= 45:
    print('cold today')
else:
    print('cold')


# 4. write a python program in which:
'''
a. the user enters either 'A', 'b' or 'C'. if 'A' is entered, the program should display the word 'Apple'' if 'B' is entered, it displays the word 'Apple'; if 'B' is entered, it displays 'Banana' and it 'C' is entered; it displays 'coconut'. use the nested if statements for this.
'''

input_letter = 'C'
#input('Please enter A, B or C: ')

if input_letter == 'A':
    print('Apple')
else:
    if input_letter == 'B':
        print('Banana')
    else:
        if input_letter == 'C':
            print('Coconut')
        else:
            print('not what was asked for!')


'''
b. repeat question a using an if statment with elif headers instead
'''

if input_letter == 'A':
    print('Apple')
elif input_letter == 'B':
    print('Banana')
elif input_letter == 'C':
    print('you can have a coconut')
else:
    print('the letter is not in the list!')


'''
c. A student enters the number of college credit earned. if the number of credits is greater than or equal to 90, 'Senior Status' is displayed; if greater than or equal to 60, 'Junior Status' is displayed; if greater than or equal to 30; 'Sophomore Status' is displayed; else, 'Freshment Status' is displayed.
'''

credits = 29.999

if credits >= 90:
    print('Senior Status')
elif credits >= 60:
    print('Junior Status')
elif credits >= 30:
    print('Sophomore Status')
else:
    print('Freshment Status')



'''
e. the user enters a number. if the number is divisible by 3, the word 'Fizz' should be displayed; if the number is dicisible by 5 the word 'Buzz' should be displayed and if the number is divisible by both 'FizzBuzz' should be displayed.
'''

number = 15

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(f'{number} is not divisible by 3 or 5')


'''
5. create a program using the schematic below to help you decide where it is okay to eat something that you dropped on the floor ...
'''



