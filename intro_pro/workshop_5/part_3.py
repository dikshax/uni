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
#    return lst_two
    return lst_three

#one = two()
#print(one)



# 3. write a python program that prompts the user to enter a list of names and stores them a list. the program should display how many times the leter 'a' appers within the list.

def three():
    names = input('please enter some names here: ')
    lst_names = [x for x in names]
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
    words = words.split()
    words.sort()
    for word in words:
        print(word)
one = four()
print(one)
