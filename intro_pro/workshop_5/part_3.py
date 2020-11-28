# 1. write a python program that prompts the user for a series of integers and stores in a list only the values between 1-100, and dislays the resulting list.
def one():
    nums = input('please enter number or numbers: ')
    lst_one = [int(x) for x in nums.split(' ') if int(x) > 0 and int(x) <= 100]
    return lst_one

#one = one()
#print(one)


# 2. write a python program that prompts the user for a list of integers and stores them is a list. for all values that are greater than 100, the string 'over' shoudl be stored. the program should display the resulting list.

def two():
    nums = input('please enter number or numbers: ')
    lst_two = [int(x) for x in nums.split(' ')]
    lst_three = []
    for x in lst_two:
        if x > 100:
            lst_three.append('over')
        else:
            lst_three.append(x)
    return lst_three

#one = two()
#print(one)



# 3. write a python program that prompts the user to enter a list of names and stores them in a list. the program should display how many times the leter 'a' appers within the list.

def three():
    names = input('please enter some names here: ')
    lst_names = [x.lower() for x in names]
    total_a = 0
    for x in lst_names:
        if x == 'a':
            total_a += 1
    return total_a


#one = three()
#print(one)


# 4. write a program that accempts a comma separated sequesnce of words as input and prints the words in a sequence after sorting them alphabetically.

def four():
    words = input('Please enter your comma seprated words: ')
    words = words.split(' ')
    words.sort()
    for word in words:
        print(word)
#four()


# 5. write a python program that rompts the user to enter integer values to populate two lists, then print messages to determine the folowing:

# a. whether the list are of the same length
# b. whether the elements in each list sum to the same value.
# c. whether there are any values that occur in both lists.

def five():
    list_1_nums = input('numbers for list one: ')
    list_1 = [int(x) for x in list_1_nums.split()]
    
    list_2_nums = input('numbers for list two: ')
    list_2 = [int(x) for x in list_2_nums.split()]

    if len(list_1) == len(list_2):
        print(f'there is {len(list_1)} numbers in list one and {len(list_2)} in list two, so they are the same length.')
    elif len(list_1) != len(list_2): 
        print(f'there is {len(list_1)} numbers in list one and {len(list_2)} in list two, so they are not the same length!!')

    if sum(list_1) == sum(list_2):
        print(f'the sum of list one is {sum(list_1)} and sum of list two is {sum(list_2)}, AND they both the same!')
    elif sum(list_1) != sum(list_2):
        print(f'sum of list one is: {sum(list_1)} and sum of list two is: {sum(list_2)}, and they are NOT the same!!')

    in_both_lists = ', '.join([str(x) for x in list_1 if x in list_2])
    if len(in_both_lists) > 0:
       print(f'{in_both_lists}, appearse in both lists.!')
    else:
        print('there is no number that appearse in both lists!!')


one = five()

















