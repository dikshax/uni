'''
1. write a program that:
'''

'''
a. uses a loop to ass up all the even numbers between 100 and 200, inclusive.
'''

# even_number = 0

# for x in range(100, 201):
#     if x % 2 == 0:
#         print(f'{x} is even and will be added to even_number')
#         even_number += x
#         continue
#     else:
#         print(f'{x} is not a even number')
# print(even_number)


'''
b. sums a series of integers entered by the user, excluding all numbers that are greater than 100
'''
# user_number = int(input('Please enter a number your highness: '))

# sum_of_number = 0

# while sum_of_number <= 200:
#     if 0 <= user_number <= 100:
#         print(f'you have entered {user_number} and it will be added to your total!')

#         user_number = int(input('Please enter a number your highness: '))
#         sum_of_number += user_number
#         print(f'your currnet total is: {sum_of_number}')

#         continue
#     else:
#         print(f'you have entered {user_number} and it will not be added to the total!')
#         user_number = int(input('Please enter a number your highness: '))
#         continue
# print(f'your total is {sum_of_number}')


'''
c. solves q2 but this time usig an infinite loop, break and continue statements.
'''
# sum_of_number_1 = 0
# while True:
#     if 0 <= user_number <= 100 and sum_of_number_1 <=150:
#         sum_of_number_1 += user_number
#         print(f'your current total is: {sum_of_number_1}')
#         user_number = int(input('please enter your number: '))
#         continue
#     elif sum_of_number_1 >= 150:
#         print(f'total: {sum_of_number_1} >= 150')
#         break



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
d. prompts the user to enter any number of positive and negative and negative integer balues. then dislays the number of each tue that were entered.
'''

# num = int(input('please enter any number: '))

# print(f'you have entered {num} and its type is: {type(num)}')





'''
2. the following while loop is meant to multiply a series of integers input by the user. until s sentinel value of 0 is entered. Indicate any errors in the code given. see if you can fix the program and get it running.
'''

# product = 1
# num = int(input('Enter first number: '))
# while num != 0:
#     print(f'{num} * {product} is {product * num}')
#     product *= num
#     num = int(input('Enter first number: '))


'''
3. for each of the following, indicate wichi is a definite loop and which n is indefinite loop, explain why>
'''

# num = input('enter a non-zero value: ')
# while num != 0:
#     num = input('enter a non-zero balue: ')

# this one looks like its a indefinite loop

n = 0

while n < 10:
    print( 2 ** n)
    n += 1

# the loop will break when n is bigger than 10
