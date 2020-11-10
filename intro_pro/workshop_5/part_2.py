# 1. for a list of integers named nums [12, 56, 72, 33, 1, 7]

# a. give a while loop that adds up all the values in nums.

nums = [12, 56, 72, 33, 1, 7]

total = 0
i = 0
while i < len(nums):
    total += nums[i]
    i += 1
print(total)


# b. write a for loop that adds up all the values in nums in which the loop variable is assigned each balue in the list

total_1 = 0
for x in nums:
    total_1 += x
print(total_1)

# c. write a for loop that adds up all the eletents in nums in which the loop variable is assigned to the index value of each element in the list.

total_2 = 0
for x in nums:
    total_2 += x
print(total_2)


# d. write a for loop that displays the elelements in nums backwards.

nums.reverse()
for x in nums:
    print(x)

print()
# e. write a for loop that displays every other element in nums.
nums = [12, 56, 72, 33, 1, 7]

e_list = [x for x in nums[::2]]
for x in e_list:
    print(x)


# 2. Give an appropriate list compreension for each of the following.
# a. producing a list of consonants that appear in a string variable

consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y']

string_variable = 'mansoud'

consonants_lst = [x for x in string_variable.upper() if x in consonants]
print(consonants_lst)

# b. prduce a list of numbers between 1 and 100 that are divisiable by 3.

nums_divisible_3 = [x for x in range(1,101) if x % 3 == 0]
print(nums_divisible_3)


# c. producing a list of temperature in Fahrenheit when given a list of temperatures in degrees Celsius.

Celsius = [123, 234, 45, 67, 20]
Fahrenheit = [round(((x * (9/5)) + 32), 2) for x in Celsius ]
print(Fahrenheit)


# 3. Define a function that ca accept two strings as input and print the string with maximum lenth in console.

def compare(string1, string2):
    if len(string1) == len(string2):
        print(string1, string2)
    elif len(string1) > len(string2):
        print(string1)
    elif len(string1) < len(string2):
        print(string2)
    else:
        print('inconcolusive')


print(compare('mansoud', 'mansoud'))
